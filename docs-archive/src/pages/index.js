import React from 'react';
import { Redirect } from '@docusaurus/router';
import versions from '@site/versions.json';

// versions.json is newest-first, so this follows the archive forward on its own
// instead of being pinned to whatever was newest when the file was written.
export default function Home() {
  return <Redirect to={`/docs/${versions[0]}/features`} />;
}
