# Solito Expo Next Notes

- **UI:** The UI of native doesn't work on the web, and vice versa. You typically have to create separate UIs for web and native. However, Tailwind is supported and works well.

- **Storybook and Jest:** Uncertain about whether to set up Storybook and Jest in separate repositories or a single repo since they share the same source code.

- **CSS for Web:** You can write CSS for the web directly from any file.

- **UI API:** You can use a UI API for the web and another for native.

- **SEO with Next:** Next looks better for SEO with a little drop-down.

- **Platform-Specific Components:** Different layouts are required for web and native.

# Next Expo

- Initially appealing when using Next for web and Expo for native in a monorepo.
- CSS utils only work on specific files, causing potential issues.

# Expo Router

- Good, but not optimized for SEO.
- Storybook and Nativewind work, but some limitations with web utils.
- Drawbacks with CSS utils and the need to use CSS, not Nativewind.

# Tamagui

- Sensitive deployment to Vercel, potential issues with Expo SDK versions.
- Attempting to solve Expo build and Vercel deployment problems.
- Three options sorted by performance: Tamagui, Solito, Expo Router.

# Solito Behavior Issues

- Unusual behavior when moving, renaming, or copying apps.
- Adding directories or apps is problematic; requires removing certain files.
- Sensitivity issues compared to Tamagui.

# Conclusion

- Three options with drawbacks: Tamagui, Solito, Expo Router.

---

# Additional Information

- **Solito Quirks:** Unusual behavior observed when manipulating Solito apps, unlike anything seen before.

- **Tamagui Compatibility:** Issues with Expo SDK versions, successful with SDK 47 but problems with Expo SDK 49.

- **Vite and Next Compatibility:** Vite doesn't work with Next as Vite is CSR, while Next is SSR.

- **Tamagui performance:** I dont understand how but when i performed my testes and did the lighthouse the results inidcates    thats Tamagui increased bundle size and reduced performance which made me to turn away about it.

- **Tamagui and Vercel:** We have not succeeded in any attempt to make Tamagui works with vercel in monorepo but it worked in repo consists of expo router only which it is the repo we performed the tests on it.

- **Tamagui and Expo:** I have tried many repos and attempt to make tamagui works but i end of faillure and i dont know if it could enhance the UI as it claims or not, one of the Attempts is to try to use pre-template made by tamagui itself and it was broken somehow becuase of lucide icons i dont understand why it broke the app and the results of this repo went so down.
**Lucide Icons:** it is svg icons but it looks kinda it can crash the app but i still dont understand how i even used resoultion and override fields inside `package.json` but it didnt work the version of react-native-svg i used was `13.9.0`.

# Image and Component Compatibility

- Image component in React Native doesn't work with Next.js.
- Imagebackground component doesn't work on both platforms.
- Some components may not work universally.

# Development Plan

- Evaluating components to determine whether to use Expo Router only or Solito with or without Tamagui.

# Development Items

- Translation by Python.
- Typography setup.
- Image setup.
- SVG icons.
- Logo setup.
- Basic component creation.
- Sound integration.
- Font and file optimization.
- Development environment setup.
- Prototype creation.

# Final Api

- **Tamagui:** Im not confident about it as the results of tests so i wont use it

- **Solito:** I would use it if i managed to get consistant style across the platoforms , but i still afraid of its weird potential, and im more affraid to cuase troubles and issues in the future or in development or the app wouldnt be stable
both **Solito** and **Tamagui** are considered new techs so im afriad of the hidden issues

- **ExpoRouter:** Actually i dont find any problem about it but it only looks Solito provide more powerfull website throw nextJs

### ***So in Conclusion:***
    - we Would use Solito or Expo router Today!