// Swizzle MDXComponents to register FeatureAvailability as a global MDX component.
// This means any .md/.mdx file can use <FeatureAvailability /> without an explicit import.
import MDXComponents from '@theme-original/MDXComponents';
import FeatureAvailability from '@site/src/components/FeatureAvailability';
import FeatureCardSection from '@site/src/components/FeatureCardSection';
import QuickstartCTA from '@site/src/components/QuickstartCTA';
import QuickstartCards from '@site/src/components/QuickstartCards';

export default {
  ...MDXComponents,
  FeatureAvailability,
  FeatureCardSection,
  QuickstartCTA,
  QuickstartCards,  // used in older versions (0.12.x – 0.14.x)
};
