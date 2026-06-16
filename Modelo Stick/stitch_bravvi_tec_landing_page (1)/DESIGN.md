---
name: Bravvi Corporate Excellence
colors:
  surface: '#f7f9fc'
  surface-dim: '#d8dadd'
  surface-bright: '#f7f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f7'
  surface-container: '#eceef1'
  surface-container-high: '#e6e8eb'
  surface-container-highest: '#e0e3e6'
  on-surface: '#191c1e'
  on-surface-variant: '#444650'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f4'
  outline: '#747782'
  outline-variant: '#c4c6d2'
  surface-tint: '#405ca1'
  primary: '#001f56'
  on-primary: '#ffffff'
  primary-container: '#123478'
  on-primary-container: '#849fea'
  inverse-primary: '#b2c5ff'
  secondary: '#bc0000'
  on-secondary: '#ffffff'
  secondary-container: '#e41f13'
  on-secondary-container: '#fffbff'
  tertiary: '#401600'
  on-tertiary: '#ffffff'
  tertiary-container: '#622600'
  on-tertiary-container: '#e48c5d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#254388'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a8'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#930000'
  tertiary-fixed: '#ffdbcb'
  tertiary-fixed-dim: '#ffb692'
  on-tertiary-fixed: '#341100'
  on-tertiary-fixed-variant: '#75340c'
  background: '#f7f9fc'
  on-background: '#191c1e'
  surface-variant: '#e0e3e6'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  stack-unit: 8px
---

## Brand & Style

The design system is engineered for a high-stakes technology consultancy, prioritizing **authority, sophistication, and modern corporate intelligence**. Inspired by the elite aesthetic of global consulting firms, the UI utilizes a refined **Minimalism** blended with **Corporate Modern** sensibilities.

The visual narrative focuses on clarity and "intellectual breathing room"—using expansive white space to denote premium service. It targets C-suite executives and technical stakeholders who value precision over trendiness. The emotional response should be one of absolute reliability, where every pixel feels intentional and every interaction feels decisive.

## Colors

The palette is anchored by a deep **Navy Blue**, extracted from the brand's identity, symbolizing stability and deep technical expertise. This is balanced against a stark **Brilliant White** background to maintain a high-end editorial feel.

- **Primary (Navy):** Used for headers, primary navigation, and core branding elements.
- **Secondary (Accent Red):** A sophisticated red is used sparingly for critical Calls to Action (CTAs) and interactive highlights, drawing inspiration from high-tier consulting visual cues.
- **Neutrals:** A scale of cool grays provides subtle structure for borders, background sections, and secondary metadata without cluttering the visual field.
- **Surface:** Pure white is the primary surface color to maximize legibility and professional "air."

## Typography

This design system employs a dual-sans-serif strategy to balance character with utility. **Hanken Grotesk** provides a sharp, contemporary edge for headlines, suggesting precision and forward-thinking. **Inter** is utilized for body text due to its exceptional legibility in data-heavy or long-form consulting reports.

The hierarchy is "top-heavy," meaning larger-than-average display sizes are used to make bold statements, while body text remains grounded and functional. Letter spacing is slightly tightened on headlines for a more "locked-in" executive appearance.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy on desktop to ensure content remains centered and authoritative, transitioning to a fluid model on smaller devices.

- **Desktop:** 12-column grid with a generous 1280px max-width. Margins are intentionally wide (64px+) to create a "letterbox" effect that focuses attention on the content.
- **Rhythm:** An 8px linear scale governs all internal spacing. Section vertical padding should be aggressive (e.g., 80px, 120px, or 160px) to maintain the premium, uncrowded feel.
- **Alignment:** Strict left-alignment for all typography to mirror professional document standards.

## Elevation & Depth

To maintain a sophisticated and flat corporate aesthetic, this design system avoids heavy drop shadows. Depth is communicated through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surfaces:** Use subtle gray backgrounds (`#F5F7FA`) to distinguish secondary content blocks from the main white surface.
- **Outlines:** Use 1px solid borders in a very light gray (`#E2E8F0`) for cards and input fields.
- **Depth:** When elevation is required (e.g., a dropdown menu), use a "Zero-Blur" or "Sharp" shadow: a very slight, high-opacity offset that feels architectural rather than fuzzy.

## Shapes

The shape language is primarily **Soft (0.25rem)**. This slight rounding takes the "sting" off sharp corners—making the technology feel approachable—while remaining sufficiently geometric to look professional. 

Avoid pill-shaped buttons or fully circular elements, as they appear too casual for a high-level consultancy. The only exception is icon containers or status indicators.

## Components

### Buttons
- **Primary:** Solid Navy background with White text. Sharp, 4px rounded corners. No gradients.
- **CTA:** Solid Accent Red background. Used exclusively for "Get in Touch" or "Schedule Consultation."
- **Ghost:** Navy 1px border with transparent background. Used for secondary actions.

### Input Fields
- Understated design: A simple bottom border or a very light 4-sided gray border. 
- Focus state: Border color shifts to Primary Navy with a 1px thickness increase.

### Cards
- White background with a subtle gray border. 
- No shadow in default state; on hover, the border color darkens slightly, and the card may lift 2px with a sharp, minimal shadow.

### Lists & Data
- Use heavy horizontal dividers (2px Navy) for section headers.
- Data visualizations should use the Navy/Gray/Red palette to maintain brand cohesion.

### Icons
- Use thin-stroke, monolinear icons. Avoid filled icons unless used as active states in navigation.