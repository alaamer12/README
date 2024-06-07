# Solito Expo Next Notes

## Solito Expo Next
- The UI of native doesn't work on the web, and the UI of the web doesn't work on native, so you usually have to create a UI for both web and native. However, Tailwind is supported and works great.

## Storybook and Jest
- Setting up Storybook and Jest can be tricky, and you might not know if it should be set for a separated or a single repo since they use the same source code.

## CSS for Web
- You can write CSS for the web directly from any file.

## UI API
- You can use a UI API for web and another for native.

## SEO
- Next looks better for SEO with a little drop-down.

## Fonts and Utilities
- You have to use fonts and other utilities for every platform. Some components like ImageBackground might not work with Next, and some native components might not work.

## Common Layouts
- You have to create different layouts for web and native.

## Expo Next
- Initially, it looks good when using Next for the web and Expo, and it is a monorepo. But there are issues with CSS utils.

## Expo Router
- It looks good but may not be optimized for SEO. Storybook and nativewind can be used with it.

## Tamagui
- Sensitive, deployment issues, peer dependencies, and problems with Expo compatibility. It worked well with Expo SDK 47.

## Conclusion
- Three options with drawbacks: Tamagui, Solito, and Expo Router.

---

# Solito App Issues
- Solito has unusual behavior when you move or rename the app, giving errors.
- Adding new directories or apps is problematic, and you may have to remove .yarn files.
- Solito is sensitive and behaves unpredictably.

# Tamagui Compatibility
- Tamagui may not be compatible with newer Expo versions. It worked well with Expo SDK 47.

# Image Components
- Image components in React Native don't work well with Next.js.
- ImageBackground components don't work on both platforms.
- Some components don't work consistently on both platforms.

# Expo Router
- Expo Router requires using native components for web, limiting styling options.
- Some CSS utilities like vw or vh don't enable HMR, requiring page reloads.
- You can use native components, but it may not be ideal for web development.

# Solito Web Compatibility
- Some CSS utilities may not work with Solito, affecting webkit compatibility.
- Complex operations in CSS may not work as expected.

# Components Evaluation
- Evaluation of components to decide if Expo Router, Solito with or without Tamagui should be used.

# Development Items
- Set translation with Python.
- Define typography.
- Set images.
- Use SVG icons.
- Create a logo.
- Develop basic components.
- Incorporate sounds.
- Optimize fonts and files.
- Set up development environment.
- Create a prototype.

---

In conclusion, these notes provide insights into the challenges and considerations of using Solito, Tamagui, and Expo Router for web and native app development.

