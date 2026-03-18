import React from 'react';

const check = (
  <svg viewBox="0 0 16 16" width="16" height="16" style={{ marginLeft: '4px', verticalAlign: 'middle' }}>
    <circle cx="8" cy="8" r="8" fill="#52c41a" />
    <path d="M4.5 8.5l2 2 4-4" stroke="#fff" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" fill="none" />
  </svg>
);

const cross = (
  <svg viewBox="0 0 16 16" width="16" height="16" style={{ marginLeft: '4px', verticalAlign: 'middle' }}>
    <circle cx="8" cy="8" r="8" fill="#ff4d4f" />
    <path d="M5 5l6 6M11 5l-6 6" stroke="#fff" strokeWidth="1.5" strokeLinecap="round" fill="none" />
  </svg>
);

const cloudIcon = (
  <svg viewBox="0 0 20 14" width="18" height="14" style={{ marginRight: '6px', verticalAlign: 'middle', opacity: 0.65 }}>
    <path d="M16.5 6A4.5 4.5 0 0012.07 2a6 6 0 00-11.6 2.18A4 4 0 004 12h12.5a3.5 3.5 0 000-7z" fill="currentColor" />
  </svg>
);

const FeatureAvailability = ({ saasOnly, ossOnly }) => (
  <div style={{
    display: 'flex',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: '0 1.5rem',
    padding: '0.5rem 1rem',
    marginBottom: '1rem',
    border: '1px solid var(--ifm-hr-border-color)',
    borderRadius: 'var(--ifm-card-border-radius)',
    fontSize: '0.9rem',
    background: 'var(--ifm-background-surface-color)',
  }}>
    <strong style={{ marginRight: '0.5rem' }}>Feature Availability</strong>
    <span style={{ opacity: saasOnly ? 0.45 : 1 }}>
      Self-Hosted DataHub {saasOnly ? cross : check}
    </span>
    <span style={{ opacity: ossOnly ? 0.45 : 1 }}>
      {cloudIcon}DataHub Cloud {ossOnly ? cross : check}
    </span>
  </div>
);

export default FeatureAvailability;
