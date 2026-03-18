// @ts-check

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'DataHub',
  tagline: 'The Metadata Platform for the Modern Data Stack',
  favicon: 'img/favicon.ico',

  url: 'https://archive.docs.datahub.com',
  baseUrl: '/',

  organizationName: 'datahub-project',
  projectName: 'datahub-docs-archive',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  plugins: ['docusaurus-plugin-sass'],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/docs',
          includeCurrentVersion: false,
          sidebarPath: require.resolve('./sidebars.js'),
          // 1.3.0 is "latest" in this archive — served without version prefix
          lastVersion: '1.3.0',
          versions: {
            '1.3.0': { label: '1.3.0', banner: 'none', path: '1.3.0' },
            '1.1.0': { label: '1.1.0', banner: 'none', path: '1.1.0' },
            '1.0.0': { label: '1.0.0', banner: 'none', path: '1.0.0' },
            '0.15.0': { label: '0.15.0', banner: 'none', path: '0.15.0' },
            '0.14.1': { label: '0.14.1', banner: 'none', path: '0.14.1' },
            '0.14.0': { label: '0.14.0', banner: 'none', path: '0.14.0' },
            '0.13.1': { label: '0.13.1', banner: 'none', path: '0.13.1' },
            '0.13.0': { label: '0.13.0', banner: 'none', path: '0.13.0' },
            '0.12.1': { label: '0.12.1', banner: 'none', path: '0.12.1' },
            '0.12.0': { label: '0.12.0', banner: 'none', path: '0.12.0' },
            '0.11.0': { label: '0.11.0', banner: 'none', path: '0.11.0' },
            '0.10.5': { label: '0.10.5', banner: 'none', path: '0.10.5' },
          },
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.scss'),
        },
      }),
    ],
  ],

  themeConfig: {
    navbar: {
      title: null,
      logo: {
        alt: 'DataHub Logo',
        src: 'img/datahub-logo-color-light-horizontal.svg',
        srcDark: 'img/datahub-logo-color-dark-horizontal.svg',
      },
      items: [
        // ── Archive badge (left of version dropdown) ──────────────────────
        {
          type: 'html',
          position: 'left',
          value: '<div style="font-weight:600;color:#ad6800;background:#fff7e6;border:1px solid #ffd591;border-radius:12px;padding:1px 10px;margin-left:8px;font-size:0.85rem;line-height:1.5;">Archive</div>',
        },
        // ── Version dropdown (Docusaurus built-in, styled below) ──────────
        {
          type: 'docsVersionDropdown',
          position: 'left',
          dropdownActiveClassDisabled: false,
          dropdownItemsBefore: [
            {
              href: 'https://docs.datahub.com',
              label: '1.4.0 (Latest) ↗',
            },
            {
              type: 'html',
              value: '<hr style="margin:0.3rem 0;opacity:0.2;">',
            },
          ],
        },
        // ── Right-side text links ─────────────────────────────────────────
        {
          href: 'https://docs.datahub.com/docs',
          label: 'Docs',
          position: 'right',
        },
        {
          href: 'https://docs.datahub.com/integrations',
          label: 'Integrations',
          position: 'right',
        },
        // ── Slack icon ────────────────────────────────────────────────────
        {
          href: 'https://datahub.com/slack?utm_source=docs&utm_medium=header&utm_campaign=docs_header',
          html: `<style>.slack-logo:hover{opacity:0.8;}</style><img class='slack-logo' src='https://upload.wikimedia.org/wikipedia/commons/d/d5/Slack_icon_2019.svg' alt='slack' height='20px' style='margin:10px 0 0 0;'/>`,
          position: 'right',
        },
        // ── GitHub icon ───────────────────────────────────────────────────
        {
          href: 'https://github.com/datahub-project/datahub',
          html: `<style>.github-logo:hover{opacity:0.8;}</style><img class='github-logo' src='https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg' alt='github' height='20px' style='margin:10px 0 0 0;'/>`,
          position: 'right',
        },
      ],
    },

    colorMode: {
      defaultMode: 'light',
      disableSwitch: true,
      respectPrefersColorScheme: false,
    },

    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            { label: 'Introduction', to: 'docs/1.3.0/features' },
            { label: 'Quickstart', to: 'docs/1.3.0/quickstart' },
          ],
        },
        {
          title: 'Community',
          items: [
            { label: 'Slack', href: 'https://datahub.com/slack' },
            { label: 'YouTube', href: 'https://www.youtube.com/channel/UC3qFQC5IiwR5fvWEqi_tJ5w' },
            { label: 'Blog', href: 'https://medium.com/datahub-project' },
            { label: 'Customer Stories', href: 'https://datahub.com/resources/?2004611554=dh-stories' },
          ],
        },
        {
          title: 'More',
          items: [
            { label: 'Latest Docs (1.4.0)', href: 'https://docs.datahub.com' },
            { label: 'Roadmap', href: 'https://feature-requests.datahubproject.io/roadmap' },
            { label: 'GitHub', href: 'https://github.com/datahub-project/datahub' },
          ],
        },
      ],
      copyright: `Copyright © 2015-${new Date().getFullYear()} DataHub Project Authors.`,
    },

    tableOfContents: {
      minHeadingLevel: 2,
      maxHeadingLevel: 4,
    },
  },
};

module.exports = config;
