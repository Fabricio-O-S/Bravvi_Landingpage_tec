---
name: High-Performance Synthesis
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#444651'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#747782'
  outline-variant: '#c4c6d2'
  surface-tint: '#3e5ba4'
  primary: '#00215c'
  on-primary: '#ffffff'
  primary-container: '#13377e'
  on-primary-container: '#87a3f1'
  inverse-primary: '#b2c5ff'
  secondary: '#00696e'
  on-secondary: '#ffffff'
  secondary-container: '#00f4fe'
  on-secondary-container: '#006c71'
  tertiary: '#102449'
  on-tertiary: '#ffffff'
  tertiary-container: '#283a60'
  on-tertiary-container: '#93a5d1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001847'
  on-primary-fixed-variant: '#23438a'
  secondary-fixed: '#63f7ff'
  secondary-fixed-dim: '#00dce5'
  on-secondary-fixed: '#002021'
  on-secondary-fixed-variant: '#004f53'
  tertiary-fixed: '#d9e2ff'
  tertiary-fixed-dim: '#b4c6f4'
  on-tertiary-fixed: '#041a3f'
  on-tertiary-fixed-variant: '#34466d'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Source Serif 4
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Source Serif 4
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Source Serif 4
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
  headline-md:
    fontFamily: Source Serif 4
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  section-padding-desktop: 120px
  section-padding-mobile: 64px
  gutter: 24px
  margin-container: auto
---

## Brand & Style

This design system establishes a premium, authoritative presence for high-performance technology consultancy. It is built on three pillars: **Executive Authority**, **Technical Precision**, and **Human Partnership**.

The visual language balances the intellectual weight of traditional management consulting with the agile, forward-thinking energy of a modern tech powerhouse. It utilizes a **Corporate / Modern** style injected with subtle **Glassmorphism** for data visualization and **Minimalist** whitespace for cognitive clarity.

The emotional response should be one of "certainty through innovation"—reassuring stakeholders of high-level strategic thinking while demonstrating a mastery of cutting-edge execution.

## Colors

The palette is anchored by the logo's **Deep Navy (#13377E)**, representing depth, stability, and executive trust. This is contrasted against an energetic **Electric Cyan (#00F5FF)** used sparingly for high-impact calls to action and technical highlights.

- **Primary:** Deep Navy. Used for headers, primary buttons, and structural branding.
- **Secondary (Accent):** Electric Cyan. Used for interaction states, data points, and urgent action cues.
- **Surface:** Clean White (#FFFFFF) and Subtle Gray (#F8F9FA) provide the "Bain-inspired" generous whitespace.
- **Gradients:** Subtle linear gradients (Deep Navy to a slightly lighter tech-blue) may be used for large backgrounds to add Accenture-style dynamism without sacrificing legibility.

## Typography

The typographic strategy employs a sophisticated pairing to bridge the gap between "Consultancy" and "Tech."

- **Serif (Source Serif 4):** Used for all headlines and display text. This provides the classic, intellectual authority of a top-tier consultancy firm. It demands attention and signals high-level strategic value.
- **Sans-Serif (Hanken Grotesk):** Used for all body copy, UI elements, and technical data. It is clean, geometric, and modern, ensuring high legibility and a contemporary, "human" feel.

Large display headlines should use a slightly tighter letter spacing for a more editorial, premium look.

## Layout & Spacing

The layout philosophy prioritizes "Generous Breathing Room." Borrowing from the Bain aesthetic, content is never crowded.

- **Grid:** A 12-column fluid grid for desktop with a maximum container width of 1440px. 
- **Rhythm:** A strict 8px base unit governs all internal component spacing (padding, margins between elements).
- **White Space:** Section vertical padding is intentionally large (120px+) to allow the user to focus on one value proposition at a time.
- **Adaptive Rules:** On mobile, margins reduce to 20px, and section padding scales down to 64px. Multi-column cards reflow to a single stack.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Soft Shadows**, avoiding heavy skeuomorphism in favor of a "Physical Digital" feel.

- **Surfaces:** Most UI sits on a base level 0 (Pure White). Cards and containers use level 1 (Subtle Gray #F8F9FA) with a thin 1px border in a slightly darker gray.
- **Shadows:** Only used to indicate interactivity or floating elements (like Modals or Dropdowns). Shadows should be extremely diffused: `0px 12px 32px rgba(19, 55, 126, 0.08)`. Note the subtle Navy tint in the shadow to maintain brand harmony.
- **Interactive Depth:** When a user hovers over a card, it should subtly lift (slight Y-axis shift) and the border color should transition to the Primary Navy.

## Shapes

The shape language is **Soft (0.25rem)**, emphasizing a professional and engineered feel over "bubbly" consumer aesthetics.

- **Standard Elements:** Buttons, input fields, and tags use the base `rounded-sm` (4px).
- **Containers:** Cards and large image containers use `rounded-lg` (8px).
- **Iconography:** Use sharp, geometric icons that mirror the "circuit" and "arrow" motifs found in the logo. Avoid overly rounded or "friendly" icon sets; prioritize thin strokes and technical precision.

## Components

### Buttons
- **Primary:** Solid Deep Navy background, white text, 4px radius. High-contrast hover state using a slightly lighter navy.
- **Secondary/CTA:** Solid Electric Cyan background with Primary Navy text for maximum "energy" and visibility.
- **Ghost:** Primary Navy border and text. Used for secondary navigation or less critical actions.

### Cards
- Clean white background, 8px radius, 1px light gray border. 
- Image-heavy cards should use a 16:9 ratio with professional photography focused on people collaborating or architectural tech environments.

### Input Fields
- Subtle gray backgrounds (#F8F9FA) with a bottom-only border that turns Deep Navy on focus. 
- Labels use Hanken Grotesk Semi-Bold for clarity.

### Photography
- **The Slalom Touch:** All photography must feature people in natural, professional settings. High-performance isn't just code; it's the people behind it. Images should feel bright, authentic, and "in the moment," avoiding overly staged stock photography.