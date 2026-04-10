# V. Raghavendran & Co - Brand Style Guide

## Overview
This document defines the visual identity and design standards for all organizational outputs including presentations, documents, websites, and marketing materials.

---

## Color Palette

### Primary Colors

**Background Color**
- **Color:** Light Grey
- **RGB:** 211, 211, 211
- **HEX:** #D3D3D3
- **Usage:** All slide backgrounds, webpage backgrounds, document backgrounds

**Accent Color**
- **Color:** Dark Blue
- **RGB:** 0, 51, 102
- **HEX:** #003366
- **Usage:** Accent lines under headings, dividers, call-to-action buttons, links

**Text Color**
- **Color:** Black
- **RGB:** 0, 0, 0
- **HEX:** #000000
- **Usage:** All body text, headings, and content

### Usage Rules
- Never use colors outside this palette unless absolutely necessary
- Maintain high contrast between text and background (black on light grey)
- Use dark blue sparingly as an accent, not for large areas

---

## Typography

### Font Family
**Primary Font:** Crimson Pro
- Available from Google Fonts: https://fonts.google.com/specimen/Crimson+Pro
- Serif font family
- Professional and elegant appearance

### Font Sizes

**Headings (H1)**
- Font: Crimson Pro
- Size: 32pt (or 2rem for web)
- Weight: Bold (700)
- Color: Black (#000000)
- Usage: Main slide/page headings

**Subheadings (H2)**
- Font: Crimson Pro
- Size: 24pt (or 1.5rem for web)
- Weight: Bold (700)
- Color: Black (#000000)
- Usage: Section titles within content

**Body Text**
- Font: Crimson Pro
- Size: 14-18pt (or 0.875-1.125rem for web)
- Weight: Regular (400)
- Color: Black (#000000)
- Usage: All paragraph text, lists, descriptions

**Small Text**
- Font: Crimson Pro
- Size: 12pt (or 0.75rem for web)
- Weight: Regular (400)
- Color: Black (#000000)
- Usage: Footnotes, captions, metadata

### Typography Rules
- Use Crimson Pro exclusively for all materials
- Maintain consistent line spacing (1.5-1.6 line height)
- Never use all caps for body text
- Use bold sparingly for emphasis within paragraphs
- Avoid italics unless absolutely necessary (prefer bold for emphasis)

---

## Design Elements

### Accent Lines
**Specifications:**
- Height: 3pt (or 3px for web)
- Color: Dark Blue (#003366)
- Position: 5pt below headings
- Width: Match the heading width or full-width of content area

**Usage:**
- Place under all H1 headings except on title/cover pages
- Creates visual separation between heading and content
- Required on all content pages/slides

### Spacing

**Margins & Padding:**
- Slide/Page margins: 40-60px all sides
- Heading bottom margin: 15-20px (including accent line)
- Paragraph spacing: 15px between paragraphs
- List item spacing: 10px between items
- Section spacing: 30-40px between major sections

**Content Layout:**
- Keep content within comfortable reading width (max 1200px for web)
- Use ample white space - don't overcrowd
- Maintain consistent padding around all elements

---

## Layout Principles

### General Guidelines
1. **Clean and Minimal:** Remove all unnecessary decorative elements
2. **High Contrast:** Always use black text on light grey background
3. **Visual Hierarchy:** Clear distinction between headings and body text
4. **Consistent Structure:** Same layout pattern across all materials
5. **No Graphics:** Avoid decorative images, icons, or template graphics unless they serve a functional purpose

### Content Structure

**Title Page/Slide:**
- Centered alignment
- Company name as H1 (no accent line on title page)
- Subtitle as H2
- Additional info in body text size
- Light grey background

**Content Pages/Slides:**
- Left-aligned heading (H1) with dark blue accent line below
- Body content starts 20-30px below accent line
- Use bullet points for lists
- Use subheadings (H2) for subsections within content
- Light grey background

---

## Application Guidelines

### PowerPoint Presentations
1. Set all slide backgrounds to Light Grey (#D3D3D3)
2. Use Crimson Pro font throughout (except slide 1 if desired)
3. Add 3pt dark blue line under headings (slides 2 onwards)
4. Use 32pt bold for slide titles
5. Use 14-18pt for body text
6. Remove all template graphics and decorations

### Word Documents
1. Set page background to Light Grey or use white for printability
2. Use Crimson Pro font family
3. Add dark blue line (3pt) under document heading
4. Follow font size guidelines
5. Maintain consistent margins (1 inch minimum)

### Websites
1. Background: #D3D3D3
2. Accent color for links and buttons: #003366
3. Text: #000000
4. Import Crimson Pro from Google Fonts
5. Use CSS to create 3px dark blue border-bottom under headings
6. Responsive design with consistent spacing

### Email Signatures
1. Use Crimson Pro if possible (web-safe fallback: Georgia)
2. Black text on light grey background
3. Dark blue accent for links
4. Minimal design, no graphics

### Marketing Materials
1. Apply color palette consistently
2. Use Crimson Pro throughout
3. Include dark blue accent lines under headings
4. Maintain clean, minimal aesthetic
5. High contrast for readability

---

## Do's and Don'ts

### ✅ DO:
- Use light grey background consistently
- Apply dark blue accent lines under headings
- Use Crimson Pro font exclusively
- Maintain high contrast (black on light grey)
- Keep designs clean and minimal
- Use consistent spacing
- Follow the visual hierarchy

### ❌ DON'T:
- Use colors outside the defined palette
- Add decorative graphics or clipart
- Use multiple fonts
- Overcrowd content
- Use low-contrast color combinations
- Skip the accent line under headings
- Use busy backgrounds or patterns
- Use emojis or informal elements in professional materials

---

## Technical Specifications

### For Designers

**PowerPoint:**
```
Background Fill: RGB(211, 211, 211)
Accent Line Shape: Rectangle, 3pt height
Accent Line Color: RGB(0, 51, 102)
Font: Crimson Pro (install from Google Fonts)
Heading: 32pt, Bold
Body: 14-18pt, Regular
```

**Web (CSS):**
```css
:root {
  --bg-color: #D3D3D3;
  --accent-color: #003366;
  --text-color: #000000;
  --font-family: 'Crimson Pro', serif;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  font-family: var(--font-family);
}

h1 {
  font-size: 32px;
  font-weight: 700;
  border-bottom: 3px solid var(--accent-color);
  padding-bottom: 10px;
}
```

**Print Materials:**
- Consider using white background instead of light grey for cost-effective printing
- Maintain all other specifications
- Dark blue accent line remains essential

---

## Accessibility Considerations

1. **Color Contrast:** Black text on light grey background meets WCAG AA standards
2. **Font Size:** Minimum 14pt for readability
3. **Font Choice:** Crimson Pro is highly legible
4. **Visual Hierarchy:** Clear heading structure aids screen readers
5. **Spacing:** Adequate spacing improves readability for all users

---

## Quick Reference

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Background | - | - | - | #D3D3D3 |
| H1 Heading | Crimson Pro | 32pt | Bold | #000000 |
| H2 Subheading | Crimson Pro | 24pt | Bold | #000000 |
| Body Text | Crimson Pro | 14-18pt | Regular | #000000 |
| Accent Line | - | 3pt | - | #003366 |
| Links/Buttons | Crimson Pro | As needed | Regular/Bold | #003366 |

---

## Version Control

**Document Version:** 1.0  
**Last Updated:** January 2025  
**Next Review:** January 2026

---

## Contact

For questions about brand guidelines or style implementation:
- Contact: Design Team / Marketing Department
- For technical support with Crimson Pro font installation or CSS implementation, consult IT department

---

**Note:** This style guide should be followed for all external and internal communications to maintain consistent brand identity across the organization.
