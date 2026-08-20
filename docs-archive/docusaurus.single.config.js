// @ts-check
//
// Single-version build config: the same site as docusaurus.config.js, limited to
// one version via `onlyIncludeVersions`. Building a single version needs far less
// memory and finishes in a couple of minutes, so it is a quick way to check a
// newly added version before running the full multi-version build.
//
// Usage:
//   ARCHIVE_VERSION=1.6.0 npx docusaurus build \
//     --config docusaurus.single.config.js --out-dir build-single

const VERSION = process.env.ARCHIVE_VERSION || '1.6.0';

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

  plugins: ['docusaurus-plugin-sass'],

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/docs',
          includeCurrentVersion: false,
          sidebarPath: require.resolve('./sidebars.js'),
          // Limit the build to a single version.
          onlyIncludeVersions: [VERSION],
          lastVersion: VERSION,
          versions: {
            [VERSION]: { label: VERSION, banner: 'none', path: VERSION },
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
        {
          type: 'html',
          position: 'left',
          value: '<div style="font-weight:600;color:#ad6800;background:#fff7e6;border:1px solid #ffd591;border-radius:12px;padding:1px 10px;margin-left:8px;font-size:0.85rem;line-height:1.5;">Archive</div>',
        },
        {
          type: 'docsVersionDropdown',
          position: 'left',
          dropdownActiveClassDisabled: false,
          dropdownItemsBefore: [
            {
              href: 'https://docs.datahub.com',
              label: 'Latest ↗',
            },
            {
              type: 'html',
              value: '<hr style="margin:0.3rem 0;opacity:0.2;">',
            },
          ],
        },
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
        {
          href: 'https://datahub.com/slack?utm_source=docs&utm_medium=header&utm_campaign=docs_header',
          html: `<style>.slack-logo:hover{opacity:0.8;}</style><img class='slack-logo' src='https://upload.wikimedia.org/wikipedia/commons/d/d5/Slack_icon_2019.svg' alt='slack' height='20px' style='margin:10px 0 0 0;'/>`,
          position: 'right',
        },
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
            { label: 'Introduction', to: `docs/${VERSION}/features` },
            { label: 'Quickstart', to: `docs/${VERSION}/quickstart` },
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
            { label: 'Latest Docs ↗', href: 'https://docs.datahub.com' },
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
