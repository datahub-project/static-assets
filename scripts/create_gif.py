#!/usr/bin/env python3
"""
Create an animated GIF from a list of PNG/image files.

Usage:
    python scripts/create_gif.py [OPTIONS] IMG1 IMG2 IMG3 ...

Options:
    --output PATH     Output .gif path (required)
    --delay FLOAT     Seconds per frame (default: 2.0)
    --width INT       Resize all frames to this width in px (default: 1200)
"""
import argparse
import sys
from pathlib import Path

from PIL import Image


def resize_image(img: Image.Image, width: int) -> Image.Image:
    """Resize image to target width, preserving aspect ratio."""
    orig_width, orig_height = img.size
    if orig_width == width:
        return img
    ratio = width / orig_width
    new_height = int(orig_height * ratio)
    return img.resize((width, new_height), Image.LANCZOS)


def create_gif(
    image_paths: list[str],
    output_path: str,
    delay_seconds: float = 2.0,
    width: int = 1200,
    white_flash_ms: int = 300,
) -> None:
    # Load and resize all frames first so we know the max height
    resized: list[Image.Image] = []
    for path in image_paths:
        img = Image.open(path).convert("RGB")
        img = resize_image(img, width)
        resized.append(img)

    if not resized:
        print("Error: no images provided.", file=sys.stderr)
        sys.exit(1)

    # Pad every frame to the tallest height on a white canvas so frames never
    # bleed through when aspect ratios differ
    max_height = max(img.height for img in resized)
    padded: list[Image.Image] = []
    for img in resized:
        canvas = Image.new("RGB", (width, max_height), (255, 255, 255))
        canvas.paste(img, (0, 0))
        padded.append(canvas)

    # Build the final frame list: content, white flash, content, white flash, …
    white_frame = Image.new("RGB", (width, max_height), (255, 255, 255))

    all_frames: list[Image.Image] = []
    durations: list[int] = []
    delay_ms = int(delay_seconds * 1000)

    for i, frame in enumerate(padded):
        all_frames.append(frame)
        durations.append(delay_ms)
        # Insert a brief white flash after every frame (including the last, for
        # a clean loop back to the first frame)
        all_frames.append(white_frame)
        durations.append(white_flash_ms)

    # Quantize to palette mode for GIF
    quantized = [f.quantize(colors=256, method=Image.Quantize.MEDIANCUT) for f in all_frames]

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    quantized[0].save(
        output,
        save_all=True,
        append_images=quantized[1:],
        loop=0,
        duration=durations,
        disposal=2,   # restore to background between frames — prevents bleed-through
        optimize=True,
    )

    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"Saved: {output}  ({size_mb:.2f} MB)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create an animated GIF from a list of images."
    )
    parser.add_argument("images", nargs="+", help="Input image files (in order)")
    parser.add_argument("--output", required=True, help="Output .gif path")
    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="Seconds per frame (default: 2.0)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=1200,
        help="Resize all frames to this width in px (default: 1200)",
    )
    args = parser.parse_args()

    create_gif(args.images, args.output, args.delay, args.width)


if __name__ == "__main__":
    main()
