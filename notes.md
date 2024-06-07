# Latest Updates goes Here!

*Note: All the data here is the updated ones, so this is the latest version.*

# V1

*Note: There's no given date*

## PC Functionalities

Here, I'm documenting my observations about my PC and its functionalities. I've encountered several issues, and I'm trying to understand their origins.

1. **Broken Functionalities:**
    - Some of my PC functionalities are not working, and I'm unsure about the cause. I suspect it might be related to missing files or an incomplete Windows update. However, I'm not entirely sure about how Windows updates work. Do they override the existing system, or do they create a new instance and delete the previous one? I think it's the former, but there's a slight possibility that the issue existed in Windows 8 and only became apparent now.
    - I'm also uncertain if these problems are related to my hardware or a package called "turbo<monorepo>" that I'm working with. The issues seem to be triggered when our project scales, resulting in larger node_modules folders.
    - One specific issue is related to file paths, which appear to have a limit of 256 characters. Interestingly, using the built-in 'copy' function in Windows failed, while performing the same operation programmatically with Python (using robocopy or shutil) succeeded. This discrepancy puzzles me, as 'copy' works well with smaller projects.

2. **Renaming Projects:**
    - Renaming a project seems to lead to file leaks and issues with reading files. However, programmatically renaming the project works without problems. The cause of this issue is a mystery, and it might be related to the "<monorepo>" structure or Windows itself.

3. **Windows Installer:**
    - Another issue I've encountered is with the Windows installer, which crashes and prevents me from installing anything. This also affects Windows updates, which used to work fine in Windows 8 and Windows 10 before my upgrade.

4. **Restore Point:**
    - Creating a restore point is no longer functioning as expected. This issue may be at the root of my problems, and, interestingly, it was working before my upgrade from Windows 8 to Windows 10.

## Other Discoveries

Here are some other observations and recommendations:

- **NPM**: Although it might seem like NPM is working, it can be deceptive. It might not show any errors, but it's not the best choice for scaling projects.

- **Yarn with Turbo**: It's not recommended to use Yarn with Turbo, especially when dealing with TypeScript configurations. Using TypeScript is essential for Turbo, and trying to avoid it by using JavaScript might not be a good idea.

- **PNPM with Turbo Monorepo**: I recommend using PNPM with Turbo monorepo projects. PNPM is efficient, lighter, and faster. However, there is a quirk with PNPM: it creates a store for dependencies, which can lead to larger node_modules directories. When you copy them, the size increases significantly, so avoid copying PNPM's node_modules.

- **Monorepo Benefits**: Working with packages in a monorepo setup is lighter and more efficient compared to working on them individually. It can significantly reduce the size of your project.

- **Package Manager Differences in Monorepos**: I also noticed something interesting about monorepos and how different package managers handle them:

    - When you're working on packages within a monorepo, they tend to be much lighter than when working on them individually.
    
    - To add to the complexity, different package managers have their unique approaches:
    
      - **Yarn**: It creates `node_modules` directories for every `package.json` it encounters. This might have some advantages, like being able to listen to nested configurations like the resolution field. If you specify the resolution field in different `package.json` files, Yarn accepts it. You also need to define the workspaces within the `package.json`.
    
      - **PNPM**: PNPM takes a different approach. It creates only one `node_modules` directory at the root. The fields like resolution in any `package.json` files, except the one at the root, will be ignored. PNPM uses a separate file to define the workspaces, although I believe it can also be written in `package.json`. Sometimes, it generates files that appear to be related to npm, but their purpose is not entirely clear.
    
      - **NPM**: npm creates `node_modules` at the root and additional ones when necessary. This means it's not necessary for every `package.json` to create its own `node_modules`. The workspaces are written in the same way as Yarn in `package.json`, and npm usually only generates two files (though there might be three in some cases, or five with Berry).
    
    - I've heard about another package manager for Windows called Rush, but I haven't had the chance to try it yet. It doesn't seem as popular as the others, so it might not offer significant advancements.

- I've looked into creating a monorepo from scratch, although I haven't attempted it yet. I'm not sure if the issues with my device are related to the monorepo structure.

- When adding projects to Turbo monorepo, I faced some challenges, especially when working with NativeWind, Storybook, and Expo Router. It worked better with RN Storybook (Expo, Native, and Web platforms) when using PNPM.

- I managed to work around the broken functionalities of 'copy' and 'paste' by implementing programmatic solutions. However, this wasn't enough to resolve all issues, and I'm still struggling to find a comprehensive fix.

- I'm concerned about potential data loss, as the restore point used to be a safety net. Losing data is a significant worry, which affects my ability to update the BIOS or get a new SSD.

- After addressing these problems, I'm left with questions about Solito and Tamagui. Will fixing these issues make them work, or are there deeper underlying problems?

- I'm also puzzled by performance discrepancies in Tamagui. My test results indicate reduced performance, while Tamagui claims performance improvements. More testing is needed to clarify this.

- I discovered that to use 'pdf2img' in Python, you need to install 'plopper' and add its bin folder to the system path.

- Additionally, you should have 'TDM-GCC-32' and 'glfw-3.3.8.bin.WIN64' in the 'C' directory to make the C++ compiler work.

- Yarn can override node_modules built with NPM, and vice versa, but PNPM cannot override others and vice versa.

Please note that my observations and recommendations are based on my experiences, and I'm still working on resolving these issues.


# V2
*Note: 
    Date: 2023/11/5.*

# Other Discoveries

Here are some other observations and recommendations:

- We have tried to use Turbo with Vercel and also adding `storybook`.

    - and firstly we failed at both, but later on, we discovered that every monorepo has to be uploaded as a monorepo to Vercel, and it can't be uploaded as a workspace. This will lead to failure. Anyway, because of discovering the error with PC functionalities [we failed to fix it], we decided to give `Solito` and `Tamagui` one more attempt. We had already made numerous attempts, but this changes everything [knowing that the failure isn't because of them but me].
    
        - we managed at first to make Solito work perfectly, but it was leaking things, and we couldn't add Storybook into it because of the failure in dependencies or by unfound story files. This is a new failure and will be discussed later. So, this is what made us turn away from Solito. But when it comes to "Does it work?" Yes, it's already working.

        - So, I thought to use Storybook as a template to add Tamagui, and I did so, but then a new error occurred. It looks like the error comes from the `Tamagui` compiler. Here, I realized it still needs time to make `Tamagui` work perfectly. Because of this, I turned away from `Tamagui` and decided, and even decided to make it with `Turbo` monorepo, but again, I failed. So, this is the end page for `Tamagui` now.

    - The second thing is trying to use `Turbo` with Vercel. At first, I failed because I haven't known that a monorepo should be uploaded as a monorepo into Vercel, even if the rest of the parts are not related to Vercel. So, in the end, I managed to use `Turbo`, and it works well.

    - For the third thing, we wanted to use Storybook in our project. Firstly, I made my attempts at `Solito` because it is the closest to what we need and well-working.

        - So firstly, we tried to add Storybook as an app to the `apps` directory [workspace], and we tried both Storybook plugins [.ondevice <Expo>, .storybook <Next.js>]. But we failed with both, and the errors are about invalid dependencies or unfound story files. So, this is everything about the first attempt.

        - So, for the second attempt, we tried to add them as workspaces under the directory [storybooks], so add under this directory [expo-storybook, next-storybook]. And again, it failed, and the error is unfound story files.

        - In the third attempt, we noticed something very important: **if there is a dependency used differently with different versions in workspaces, even if they aren't related to each other, this dependency can cause crashing the monorepo. So, you need to take care of the dependencies you are installing because conflicts equal crashing**. So after knowing that, we fixed the dependency versions and, hurray! It worked, but it doesn't work well. For more clarification: it doesn't update any state or story file, and even if you tried to use the script of Storybook to update it, it failed and gives an error we don't understand, like it is related to something we don't know. So again, in the end, this attempt is considered failed, even if it worked partially, which isn't correct.

        - For the fourth attempt, we did a little search and found out that the reason it wasn't working [probably] in attempt three was because it needs a builder, and I haven't thought of that because it works well when it stands alone in the repo. But I didn't know in a monorepo it usually requires a different builder than webpack, and the builder is Vite. I found many uses Vite as a builder for a monorepo, but at first, I thought it won't work because the monorepo has React Native code, and Vite compiles React. But somehow, it works. Finally, after all of these attempts, it works. But actually, we haven't added Vite by ourselves or configured it. We actually found that `Turbo` provides a monorepo template with Storybook, and it uses Vite as a builder. But something special about this repo is it was using Storybook in packages, which we haven't tried to use Storybook at all. I have seen other repos on GitHub, and some of them use Storybook in packages/design-system [instead of the designs directory]. But this repo was old with old dependencies [SDK 46, Next 12v].

        - So from here comes a new attempt to make the perfect monorepo we need that contains everything.

            - And again, we started our first attempt, and it was to add Next.js to this monorepo of `Turbo` because this monorepo was only having Storybook while the normal monorepo of `Turbo` has Next.js. Anyway, we tried to add Next.js to it, and we failed. But it looks like the error is related to the compiler of ES because in the README file of the repo, it explains it used a new way to work with Storybook, which is `tsup`, and `tsup` looks like a compiler for ES, but it also used Vite. And I'm thinking maybe there is a conflict in dependencies [I don't think so because the error doesn't look so], or maybe the error the `tsup` isn't compatible or needs config for Next.js. I really don't know, but I haven't tested too much because there is another error which is unfound story files. Again, this error is repeated too many times, and I don't know where it comes from, how to solve it, or if it is known or something like that. Does the error relate to Storybook v7 in monorepos or what? But what I know is it fires when copying the monorepo with its dependencies [even with robocopy] or sometimes I don't know when. But I think this error occurs in monorepos only because of their complicated structure. I have noticed that you have to make the alias paths into Storybook and tell it what to compile, and so on. So, in the end, Storybook has a bug in monorepos, and it requires more config and a builder where it gives unfound story files. Next.js didn't work with tsup, with some working around.

            - For the second attempt, we got a feeling we aren't going anywhere with Turbo, so we decided to go back to `Solito` for further tests to make it perfect. After a little searching again, we found a repo that uses Storybook with `Solito`, so we tested and... **HURRAY!!**, it worked. We tested Storybook, and it worked. We tested Next, and it worked. We tested Expo, and it worked. We tested Tailwind, and it worked. We tested CSS, and it worked. We tested dependencies, and it worked. We tested scripts, and it worked. **HURRAY!!!!** We are one step closer to the best monorepo, and the last test is to make it the perfect monorepo for us, is to test `Moti` 😄, **BUT** 😢 it threw an error, and I found a lot of people telling it is a headache to make `Moti` work with it. Really, I don't know what the problem is that makes Storybook doesn't work with `Moti`. Is it because of the Vite config or Storybook config? The only thing I know is that Moti uses `.mjs` files which need to be compiled, and it looks like the workaround with it. Without `Moti`, we can't show any animation on Storybook, which is not nice. So we thought about adding `.ondevice` to Storybook, but we don't know how to add it or where, and we tried to change the config, and this led to an error, and we tried to use some other dependencies, resolutions, and we failed.

            So for now, we couldn't solve this issue, and we don't know if it is solvable or not. So we tried to use something else other than `Moti`, and we tried `reanimated`, and it looks like the error comes from `reanimated`. That's what made `Moti` not work because `Moti` is a layer or wrapper of `reanimated`. But we tried the built-in `animated` in React Native, and it worked, but it's not the animation we need. I also know we can use CSS animations, but this would be more effort and harder. So in conclusion, we decided to use this monorepo, and we will try to work around this little issue, with hopes it gets resolved.

    - So, to clarify things that haven't been cleared:
    
        - The unfound story files: is an error that tells that the compiler or builder didn't find any story files, even if the main.js content field is configured perfectly, and I don't know why it doesn't. So.

        - Vite has a little thing you need to take care of: the JSX code should be written in a .jsx file, or it will raise an error or won't be compiled. So the previews.js in Storybook have to be previews.jsx because it uses JSX. You can also provide aliases to extensions if you don't want to change file extensions.

        - In every attempt we did or test, I want to say we used every possible known package manager. This means we have tested all the tests again and again and again with [Yarn, Berry, Npm, Pnpm]. Mostly, Pnpm fails, and some of Berry, and I think Npm did well in all, but I still don't like it.

        - Moti didn't work in a normal repo, but with some effort, we made it work perfectly. So I think we can also do this for the monorepo.

        - Storybook should have some config in pipelines with Turbo, and I don't know if it's necessary.

        - Storybook can work without submodrn in the config.

        - Storybook essentials are 6 APIs in v7 and 4 in v6.

        - We haven't tried src directory in our monorepo, but I think it should work normally.

        - Prettier was making errors in some dependencies when using Npm only.

        - Yarn gives an error if you are installing dependencies that aren't compatible with your PC hardware, while Npm and Pnpm ignore it.

        - Npm doesn't understand "workspace:" as a value in monorepo, so you have to use "*" or the real version.

        - We don't know what tsup is, and we don't know if Next is going to work without it because when we tried Next with it, we used tsup.

        - We don't know any alternative for Moti, especially Solito uses it, and using another one may give a conflict. So `Moti` is the only solution to use if you are going to use this monorepo. However, it works well but not for Storybook.

        - We don't know if the UI components for Tailwind are going to work universally perfectly or not, or if they will work at all.

        - We don't know if the plugins for Tailwind are going to work universally or not.

        - It looks like in the Vite config there are files [index.html, index.css], so I don't know if those files are affecting the output or just for configuring, or do they only affect Storybook.

        - Adding ondevice, then removing it crashes the monorepo dependencies.

        - Turbo generators didn't work, but I think there is a mistake from me, so I think it would work greatly.

        - If we are still going to use this monorepo and the plugins failed to work universally, this will lead to more effort from us and making our UI components, especially for web and native.

        - We checked that the logic can be shared; there is no problem. 🤔

# V3
*Note: 
    Date: 2023/11/12.*

    ## First Challenge: Fixing Solito with Moti in Storybook

Firstly, we dove into working with Solito. The initial hurdle was Moti in Storybook. We tackled the "setimmediate" error by realizing our misstep – declaring "__DEV__" in main.js instead of vite.config. However, the real culprit was Reanimated, not Moti. After numerous attempts, we successfully integrated it into Storybook by placing the necessary files in preview.js.

### Observations:
- Config order matters.
- Reanimated may not visually animate but works without errors.
- Moti, our preference, works seamlessly.

## Second Challenge: Navigating `.ondevice` and `.env`

Next, we explored `.ondevice` but faced issues related to React Native and `.env` files. Attempts with `dotenv` and `dotenv-mono` led to an epiphany: `react-native-dot-env` is the solution for React Native. However, it requires an import statement instead of the usual `process.env`.

### Insights:
- Web and native configurations differ.
- `react-native-dot-env` requires imports.

## Third Challenge: Understanding Eslint, Prettier, and Tailwind

In this phase, we delved into configuring Eslint, Prettier, and Tailwind. The journey involved testing `prettier-eslint-config` and integrating various addons. Achieving compatibility with both Eslint and Prettier marked a significant win.

### Note:
- Prettier may fall short compared to Eslint.

## Universal Components: Integrating Third-Party Packages

Our quest for universal components led us to integrate `react-native-paper` with Next.js. Overcoming challenges with import statements, we discovered the power of the `dynamic` import statement for successful integration.

### Considerations:
- Indirect imports impact the bundle.
- Error handling differs between local and Vercel environments.

## Testing Solito Components: Overcoming Image Challenges

Testing Solito components posed challenges, especially with image components. We introduced `SolitoImage` for universal image handling, addressing Expo's limitations with relative paths.

### Discoveries:
- Image path handling varies between Expo and Next.js.
- Successful use of `react-native-svg` on native.

## Tailwind Tests: Navigating Styling Challenges

Tailwind tests revealed varying success with native styles. Some styles failed, and plugins appeared to work only for the web.

### Insights:
- Tailwind alters tag behavior.
- Successful SVG icon use with specific considerations.

## Further Tests and Discoveries

- Ongoing tests planned for videos, animated images, Motify components, Lottie, sound, and file inputs.
- Exploring library compatibility with Tailwind for global functionality.
- Emphasizing the importance of making components into modules for proper tree shaking.

## Additional Insights

- Considering potential global functionality of component libraries with Tailwind.
- Emphasizing the need for module creation, even for unchanged components.
- Introducing accessibility considerations in React ESLint.

## Conclusion

The journey involved overcoming challenges, gaining insights, and planning for future tests. The roadmap underscores the importance of meticulous configuration, platform-specific considerations, and ongoing testing for a successful cross-platform project.

# Another response V3
    # V3

- **Solito Configuration:**

  - Established work with Solito, addressing Moti issues in Storybook.
  - Noted the challenge with Moti related to the Reanimated environment.
  - Configuration struggles in `vite.config` and the realization that `main.js` is the fitting place.
  - Resolved the `setimmediate` error by placing necessary imports in `preview.js`.

    - **Observations:**
      - Order matters, and Reanimated may not visually animate but functions without errors.
      - Moti is our choice, working seamlessly.

  - **.ondevice Challenges:**
    - Explored using `.ondevice`, faced React Native and `.env` issues.
    - Tried different configurations, including `dotenv-mono` and `react-native-dot-env`.
    
    - **Insights:**
      - .env usage varies between React Native and the web.
      - Configurations differ for web and native.

  - **Eslint, Prettier, and Tailwind Setup:**
    - Configured eslint, prettier, and Tailwind with VS Code extensions.
    - Tested `prettier-eslint-config` and added various addons.
    - Achieved integration with both eslint and prettier.

    - **Note:**
      - Prettier may not handle all cases; eslint is more effective.

- **Universal Components:**

  - **Third-Party Package Integration:**
    - Faced challenges integrating `react-native-paper` with Next.js.
    - Overcame challenges with `dynamic` import statements for universal use.
    - Discovered the need for indirect imports.

    - **Considerations:**
      - Indirect imports may impact the bundle.
      - Addressed Vercel errors with `patch-package`.
      - Noticed differences in error handling between local and Vercel.

  - **Testing Solito Components:**
    - Overcame image component obstacles for universal compatibility.
    - Introduced `SolitoImage` for handling images universally.
    - Explored limitations with Expo handling relative paths.
    
    - **Discoveries:**
      - Different handling of image paths in Expo and Next.js.
      - Successful use of `react-native-svg` on native.

  - **Tailwind Tests:**
    - Conducted tests on Tailwind, noting varying success with native styles.
    - Identified issues with certain styles not supported in native.
    - Explored plugin usage, noting limitations on native platforms.

    - **Insights:**
      - Tailwind may alter tag behavior.
      - Successful use of SVG icons with specific considerations.

- **Further Tests and Discoveries:**

  - Planned future tests for videos, animated images, Motify components, Lottie, sound, and file inputs.

  - **Library Observations:**
    - Explored compatibility of component libraries with Tailwind.
    - Emphasized the importance of making components into modules for proper tree shaking.

  - **Accessibility and Styling:**
    - Introduced accessibility considerations in React ESLint.
    - Explored dimensions, styles, and ratios for better cross-platform compatibility.

- **Additional Insights:**

  - Considered the potential global functionality of component libraries with Tailwind.
  - Emphasized the need for module creation, even for unchanged components.

  - **React ESLint Tips:**
    - Discussed providing accessibility names for components.

## Conclusion

The journey involved overcoming challenges, gaining insights, and planning for future tests. The roadmap underscores the importance of meticulous configuration, platform-specific considerations, and ongoing testing for a successful cross-platform project.


# V5 - My Journey with Tailwind, Expo, and Testing

## Tailwind Troubles

- Tested a bunch of Tailwind components. Some used classes, others like Flowbite used components.
- The class-based ones didn't give me any grief on native, but they didn't render as expected.
- The component ones, on the other hand, threw a native error about box shadows. Manually adding box shadows worked but still wouldn't render. Weird, right?
- No luck finding a Nativewind UI component. But wait, stumbled upon an Expo template by Obytes on their site.

## Obytes Expo Template Exploration

- This Expo template is like a pro-level app. Uses auth through zustand and mmkv, supports dark mode, and even has Arabic. Fancy!
- Had an aha moment about the importance of the env file and their unique structure.
- Expo supports 4 build profiles (development, staging, test, production). Pretty handy!
- Explored Jest, EAS hooks, and this new thing called Maestro for E2E testing on phones. Maestro gave some EAS errors (fixed later, details coming).
- Tried installing Maestro, but alas, no release for Windows. WSL to the rescue? Nah, let's try something else.

## Dive into Deployment Patterns

- Expo has solid documentation on deployment patterns. Next.js? Not so much.
- Learned about the staging phase importance in deployment. Also watched YouTube videos on deploying to Google Play and testing on it.

## Testing Frameworks Quest

- Realized to make our dream template, we need testing utils and frameworks in place. Jest for unit testing, React Testing Library for component testing, and two E2E testing tools (one for native, one for web).
- Explored native E2E testing options - Detox and Maestro. Detox gave us a run for our money with some permission errors.

## CI/CD and Other Tools Dilemma

- Explored CI/CD tools - Travis, CircleCI, GitHub Actions. Still not sure if we need them. They seem to consist of workflows and actions. Need to figure this out soon.
- Discovered validation libraries - Zod, Joi, and more. Obytes app uses these to define the development phase.

## Other Nuggets of Wisdom

- Unicorn ESLint plugin, a mystical creature that helps in linting.
- Unearthed a weird bug in Storybook. Turns out, para brackets in the path caused the "no story files found" error. What a quirk!
- Experimented with Detox - fixed some EAS errors, but then hit a roadblock with emulator issues.

## Detox Drama Continues

- Detox drama escalated. Had to put `bash` before commands to make it work on EAS. Emulator still not waking up. Expo docs say Detox has issues with Android (but shines on iOS).
- Realized Detox needs two builds - one default release build (`expo run:android`) and another Detox-specific test build (run `gradlew`, not `./gradlew`).

## Understanding Detox and Maestro

- Detox - great for isolated testing (single repo). Hope it behaves the same in a monorepo.
- Unclear about Detox and Maestro's workings. Do they just check if JS code executed or dive into native abilities? React Native docs hint at JS-only checks.

## Component Usage Dilemma

- Realized we need a game plan for using components. How's our pattern gonna be? How do we reuse modules?

## Testing Libraries Hurdles

- Tried Expo/@testing library. Path error galore - wants to use node utils, but React Native doesn't vibe with it. Not sure if Expo really tested this lib.

## Yarn PnP Compatibility Saga

- Playwright, Cypress, and friends aren't pals with Yarn's PnP. Expo hinted PnP has no compatibility yet. But hey, Yarn Berry version 3.4 to the rescue!

## Random Tech Tidbits

- Tried @react-native-material/core - error in React Native, but no clues in the abyss.
- Gave responsive fontsize one last shot for the web. Tailwind still playing hard to get.

## Viewport Unit Shenanigans

- Found new units - lvh (large viewport height), dvh (dynamic viewport height), svh (small viewport height).
- Also, the named export seems cooler than the default one. Who knew?

## Tailwind Theme Victory

- Settled on a Tailwind theme - tested and approved. Variables playing nice too.

## Fonts and Expo Mysteries

- Figured out how to use fonts API in Next.js. Fonts set for all platforms.
- Still confused about special styles for API 17, 21, and iPhone X. A mystery to solve later.

## Playwright vs. Cypress Showdown

- Threw down a Playwright vs. Cypress showdown. Cypress is the cool kid in town, but Playwright has tricks up its sleeve too.

### Cypress:

- Easy to integrate, configure, and use.
- Unique DOM manipulation.
- Supports Chrome, Electron, MSE.
- Captures screenshots during test execution (comprehensive test insight).
- Friendly debugging, readable errors, works with developer mode.
- Unique built-in waiting, no need for `sleep(time)`.
- Functionality-like unit testing with server response, timers.
- Allows network traffic manipulation.
- Cypress Studio with record tools (config in the file).
- Better syntax, non-developer friendly.
- Perfect documentation.
- Good built-in parallelism for instances and machines.
- Provides utils for HTTP requests, validations, assertions, etc.
- Offers mocking, especially for APIs.
- Plugins for APIs, comprehensive for real and remote devices.

#### Test Flakiness Solutions:

- Reduced test flakiness with a proper promise.
- Auto-waiting and retry.
- Control over test runner and environment.

#### Considerations:

- Can't make instances multi-browser simultaneously.
- Lack of multi-tab testing.
- Recommends using JavaScript.
- Limited mobile support, but supports phone viewports.

### Playwright:

- Works directly through WebSocket instead of HTTP requests.
- Own protocols for browsers, cross-browser support.
- Runs complex tasks - spanning multi-page and multi-domain.
- Network manipulation with differences from Cypress.
- Enables file upload and downloading scenarios.
- Native input tests, enhanced testing through browser context, parallel test execution.
- Integrations with CI/CD, Docker, cloud systems.
- Code generation - generates code as you interact with the browser.
- Async test code, comprehensive mobile support.
- Functionalities for URL and API manipulation, validations, custom assertions, etc.
- Auth and security functionalities.

#### Test Flakiness Solutions:

- Uses advanced features for reliable testing.
- Async code and promises for reliability.
- Built-in wait, network manipulation, interception.

#### Considerations:

- Steeper learning curve.
- Smaller community compared to Cypress.
- Limited extensions and tutorials.
- Needs improvement in documentation.
- Test runner support for parallelism needed but provides faster execution.
- Cypress considered used by 2x or more than Playwright but Playwright ranked number 1 in most intersted.




# Version 6 Release Notes

This version was developed in a relatively short timeframe compared to previous releases, yet its significance lies in the information it provides. Here's a summary of the key points:

## Continuous Integration and Continuous Deployment (CI/CD)

We delved into CI/CD, understanding their purpose, applications, and operations. While the knowledge gained may not be exhaustive, it is substantial. 

- **CI/CD Overview:**
  - CI/CD automates tedious tasks, such as error detection, bug fixing, ensuring good commits, and handling conditions like pull requests or pushes.
  - Additional packages, like `husky` and `lint-staged`, enhance effectiveness.
    - `husky` extends `git` functionality through hooks, with a common example being the pre-commit hook.
    - `lint-staged` operates post-commit, ensuring selective application of tasks only to changed and committed files.

- **CI/CD Vendors:**
  - Over 40 vendors exist, with many offering free trials or being entirely free.
  - Examples include GitHub Actions, GitLab CI, Travis CI, CircleCI, Jenkins, Bamboo, TeamCity, etc.

    - **GitHub Actions:**
      - Free with limitations.
      - Cloud-based, integrates seamlessly with GitHub, and supports multi-container operations using Docker.

    - **GitLab:**
      - Not free, but offers a free trial.
      - Deeper integrations, advanced caching, and support for parallelism.

    - **Travis CI:**
      - Not free, but provides a free trial.
      - Supports various languages, prioritizes privacy and security, offers self-hosting, and integrates with cloud services.

    - **CircleCI:**
      - Free with paid plans available.
      - Easy setup, widely used in large-scale projects, supports various version control systems, and has advanced testing features.

- **Decision Process:**
  - Narrowed down choices to GitHub Actions and CircleCI, considering project requirements and prerequisites.

- **Observations:**
  - GitHub Actions and CircleCI are commonly used, but the recognition of other CI/CD tools in GitHub repositories remains uncertain.

- **Decision Factors:**
  - Preference for simplicity and ease of use favors GitHub Actions and CircleCI over alternatives like Jenkins or TeamCity.

## Environment Files and Variables

In the context of the next project, insights were gained regarding environment files and variables.

- **NEXT_PUBLIC_ Prefix:**
  - Variables with the prefix NEXT_PUBLIC_ can be exposed and rendered as text.
  - Other environment variables encounter rendering issues, displaying errors even when defined and functional.

- **Git Branch Strategy:**
  - Discussed the relevance of using a Git branch strategy, even though CI/CD is prevalent. Proposed branch categories include feature[s], testing/envy, fix[er], and crowdy.

- **Glob Patterns:**
  - Learned about glob patterns, simplified string patterns used for configuration and path matching.

- **Node Environment (NODE_ENV):**
  - Explored considerations for NODE_ENV across Next.js and Expo, highlighting the challenges and recommended practices.

# Sixthly

In our project, there's a need for a help center, about page, or similar components. Various methods exist to implement these, but the primary concern is the budget. Three common approaches are noted:

- **Slug-page:**
  - Incorporates a slug for sections like help center or about within the main domain (e.g., `https://example.com/help`).
  
- **Custom-domain:**
  - Prefixed domain with a keyword for sections (e.g., `https://custom<about>.example.com`).
  
- **Different-domain:**
  - Uses entirely different domains (e.g., `https://examhelp.com`).

The cost-effective choice is the slug-page method, leveraging the same domain. However, potential future scalability issues may arise since these sections are static in Next.js, and SSG or ISR is preferred.

- **SSG (Static Site Generation):**
  - Generates pages at build time.
  - Disadvantages include extended build times for a large number of pages.
  
- **ISR (Incremental Static Regeneration):**
  - Addresses the SSG drawbacks by incrementally regenerating pages.

# Seventhly

## Node Process and Project Structuring

### Node Process:
- Gained insights into the node process module, particularly the use of `process.env` and `process.argv`.
- Compared to JS or Python, C++ lacks a standard file for packages (similar to `package.json` in JS).
- Recommended using ES5 syntax when uploading a package to npm for broader compatibility.

### Project Structuring:
- Observed different approaches in large-scale projects for breaking down the project.
  - Scoped packages like `@vscode` used in VSCode.
  - Internal packages used within the repository in projects like React.
  - Dedicated packages directory (workspace) in projects like Next.js.

### Versioning and Release Types:
- Differentiated between canary, experimental, prerelease versions, and LTS.
- Described various prerelease versions such as alpha, beta, rc, along with their meanings.
  
# Eighthly

## GitHub Actions, Docker, and Miscellaneous Files

### GitHub Actions and CircleCI:
- Noted the use of both GitHub Actions and CircleCI in repositories, with CircleCI often employed for Docker actions.

### Docker:
- Differentiated between Docker with-compose and without-compose.
- Introduced the `MakeFile` as a file for automation tasks, commonly used for Docker-related tasks.

### Miscellaneous Files:
- Introduced the `manifest.json` file used in web development to provide configuration information.
- Mentioned the importance of files like `twitter-image` and `opengraph-image` for link previews on social media.

### Data Format Files:
- Discussed various data format files like XML, JSON, YAML, and TOML.

### Operators:
- Introduced relatively new operators like `??`, `?.`, `!`, and `!.`.

# Ninthly

## JavaScript Techniques

- Explored chainable functions in JavaScript, discussing two approaches: using a class or nesting functions within a function.
- Introduced the use of the `super()` constructor in JS when a class extends another class.

# Seventh Version (V7)

## Firstly

### Playwright and Testing

- **Playwright:**
  - Acknowledged the power of Playwright with its various utilities and functionalities.
  - Emulation capabilities for time zones, geolocation, and strong support for iPhones (emulator test runner).
  - Limited Android support, requiring hardcore setup, stay awake settings, and reliance on adb or avm for native tests.
  - Mentioned the difficulty in using raw USB for native tests.
  - Attempted the use of Storybook addon for Playwright but faced issues, possibly due to maintenance or Playwright being considered newer tech.
  - Encountered errors with the Jest addon of Storybook, potentially related to Vite builder, leading to the exploration of vitest as an alternative.

## Secondly

### Insights into package.json

- **Package.json Knowledge:**
  - Introduced the `funding` field as a way to provide a URL for funding or support.
  - Discussed the `files` field, which covers repository files when used as a dependency.
  - Mentioned the `.npmignore` file, which cannot override the root `files` field but can override subdirectories.
  - Differentiated between the `main` and `browser` fields based on the intended environment (node or browser).
  - Highlighted the utility of the `bin` field in accessing the PATH and adding executable files.
  - Introduced the `directory.bin` field for loading an entire directory of binaries.
  - Discussed the `man` field for Unix-based documentation and the `directory.man` field for loading an entire directory of man files.
  - Briefly explained the `repository`, `dependencies`, `cpu`, `os`, and `engines` fields.

## Thirdly

### Storyshot Addon and New Technologies

- **Storyshot Addon and Markup Languages:**
  - Explored the use of the Storyshot addon with Puppeteer and Jest, encountering errors and deprecation issues.
  - Shifted to the test-runner addon, encountering some build challenges yet to be resolved.
  - Speculated on potential solutions, considering familiarity with Vite.config or Rollup.
  - Introduced alternative markup languages like .rst, noting their richer feature set compared to .md.
  - Explored the new technology called Sentry for crash and analysis, comparing it with Firebase's analytics and crashlytics.
  - Discussed the limitation of Firebase's free event threshold and found a comparison of different error logging tools (Sentry, Rollbar, Bugsnag).
  - Explored the strengths of each tool and leaned towards Sentry or Rollbar for further consideration.
  - Mentioned considerations such as dashboard quality, commit tracing, integration, and essential features when choosing an error monitoring tool.
  - Noted that Sentry is trusted by React Native and Expo, while Rollbar is perceived as more advanced.

## Conclusion

- Explored the use of MakeFile as a sub-language with its own syntax, primarily used with C and C++.
- Highlighted the utility of MakeFile in compiling changed files and automating tasks in C and C++ projects.
- Summarized useful points to consider when choosing an error monitoring tool.


# Fourth Version (V4)

## Fourthly

### React-Native, Flutter, and Native Platforms

- **React-Native and Flutter:**
  - Acknowledged that React-Native and Flutter may not share many concepts despite being cross-platform.
  - Shared knowledge about package managers and configuration files in Flutter (pubspec.yaml) and Swift (Package.swift and CocoaPods with Podfile).
  - Expressed uncertainty about finding common concepts in native platforms but expressed the intention to explore and advance in React-Native, Flutter, Cordova, Ionic, Android, iOS, and Unity.
  - Mentioned the challenges in integrating Unity within React-Native, especially with Expo.
  - Noted that communication with Unity is possible through native code.

## Fifthly

### Async Code and Callback Functions

- **Async Code:**
  - Provided an in-depth understanding of async functions, promises, and callbacks.
  - Explained the three states of promises (pending, fulfill, reject).
  - Contrasted callback hell with promises, highlighting the asynchronous nature of both.
  - Discussed the importance of using `await` to ensure code execution in sequence.
  - Explained the compatibility issues of normal iterators (e.g., `forEach`) with async code and introduced `for..of` as a compatible iterator.
  - Showed alternatives to using `await` with `return new Promise`.
  - Demonstrated three common ways to execute async functions.

## Sixthly

### APIs and Databases

- **Choosing an API Framework:**
  - Discussed the considerations in choosing an API framework, specifically in Python.
  - Explored Django, Flask, and FastAPI, with considerations for scalability.
  - Emphasized Django's suitability for large-scale projects but mentioned potential challenges with async functions.
  - Noted the opinionated nature of Django, offering less flexibility.
  - Mentioned the need to learn more about APIs and databases as the app scales.

- **Async Functions in Django:**
  - Mentioned considerations for handling async functions effectively in Django.
  - Raised awareness of the potential lock-in and opinionated nature of Django.
  - Indicated that Django is the chosen API framework for Python.

- **Overview of APIs and Databases:**
  - Introduced architectural patterns in APIs (MTV, Event-Driven, MVC, RESTful, Microservices).
  - Highlighted the importance of understanding various API and database options.
  - Mentioned polyglot persistence and its potential benefits.
  - Described polyglot databases and the possibility of using multiple databases simultaneously.

- **Looking Forward:**
  - Acknowledged the need to understand APIs, databases, RESTful, GraphQL, and more.
  - Emphasized the importance of determining frameworks, protocols, and the mechanics of APIs.
  - Mentioned the integration of small APIs using Prisma in NextJs.
  - Concluded with the recognition of the long journey ahead, especially concerning AI models and the purpose of the API.


# V8

Anyway, I don't remember much, but this time, we took a different direction. We focused on understanding more about the backend.

With all the related things we've done before, we compared different frameworks in various languages for building an API. Our winners are Django and Node.js (NestJS for Node.js backend framework). NestJS seems preferable as it's likely built over Express, can use Fastify under the hood, primarily uses TypeScript, and follows an Angular-like structure.

NestJS appears superior in terms of scalability. Here arise two questions:
1. Why are there two winners?
2. Why are Node.js frameworks the second winner? (We already know why Django is the first winner.)

Firstly, there are two winners because we're making two or more APIs. One for AI (Django won), and the second API will handle the database and related tasks.

Secondly, Node.js frameworks won because we're familiar with NestJS, and exploring other languages won't expedite our development. Also, React Native and Next are based on the Node.js runtime, leading to less or zero configuration. Node.js has a broad ecosystem with many libraries and tools.

Based on this, we explored options not only for APIs but also for databases and backend.

Initially, we considered Firebase, but vendor lock became a significant concern. So, we had three options:
1. Take the risk and use Firebase.
2. Use an alternative to Firebase, like Supabase, without vendor lock.
3. Build our own from scratch.

Each option has its pros and cons.

- First option [high productivity, less control]:
  - Pros: One-liner framework, scalable, advanced, provides many things out of the box, adapted for BaaS, advanced database operations.
  - Cons: Vendor lock, high cost.

- Second option [moderate productivity, moderate control]:
  - Pros: Comparable to Firebase, lower cost, uses PostgreSQL, no vendor lock.
  - Cons: Not as advanced as Firebase, smaller community, limited, high cost.

- Third option [less productivity, high control]:
  - Pros: Full control, lighter dependencies, self-managing, fully customizable, free to low cost.
  - Cons: Time-consuming, may not be as efficient or professional as a service provider.

Considering the future, we think the second and third options are better, avoiding vendor lock.

Our journey into backend development involves choosing a suitable database. Criteria include real-time communication, alignment with our schema, global usability, scalability, and more.

Next, we need to choose tools. Options include Raw SQL, SQL query builders like Knex, ORMs like TypeORM, and Prisma. We need to consider compatibility, productivity, extensibility, scalability, and integration with frameworks like NestJS.

The next steps involve deciding on the API style (RESTful, GraphQL, SOAP), choosing backend frameworks, using tools for API development, selecting hosting for the API, establishing a connection between backend and frontend, and completing the backend.

A note: Backend isn't just about handling messaging data; it can manage the entire system. Common API architectures include RESTful and GraphQL. Understanding your case is crucial for selecting real-time communication tools like WebRTC and Socket.IO.

Additionally, we touched upon SAML and CIAM used in large companies.

Beyond backend, we delved into other terms, such as React Native, where we explored libraries like Victory Native, and encountered challenges with Realm SDK for Expo.

We also learned the benefits of using Docker for backend development and explored tools like Tauri, Electron, and NX.js to convert websites into executable desktop applications. Each tool has its strengths and weaknesses, and the choice depends on application dependencies and requirements.

Lastly, Next.js supports MySQL, PostgreSQL, and MongoDB out of the box, with other databases possibly requiring additional configurations.


********************************************************************
# **Another response**

# V8

In our recent exploration, our focus shifted towards the backend, specifically delving into backend frameworks for API development. Through comparisons across various languages, two standout winners emerged for our APIs: Django and Node.js (specifically NestJS). NestJS, with its default integration over Express and the option to use Fastify underneath, caught our attention. Its primary reliance on TypeScript and an Angular-like structure further bolstered its appeal.

The preference for two winners stems from our intent to create multiple APIs. Django is our choice for the AI-centric API, while the second API, responsible for handling databases and related tasks, leans towards Node.js frameworks. NestJS stands out as our preferred choice due to its scalability and overall efficiency.

This decision raises two fundamental questions:
1. Why do we have two winners?
2. What makes Node.js frameworks the second winner? (Given that we've already identified Django as the primary winner.)

The dual-winner strategy is driven by our need for distinct APIs—one for AI (where Django excels) and another for managing databases.

The choice of Node.js frameworks as the second winner is grounded in our familiarity with NestJS, making it a pragmatic choice. Additionally, the alignment with React Native and Next, both rooted in Node.js runtime, contributes to streamlined development with minimal configurations. The extensive Node.js ecosystem further reinforces our decision.

Our exploration extends beyond APIs to encompass databases and broader backend considerations. Initially considering Firebase, concerns about vendor lock prompted us to evaluate three options:

1. **Risking with Firebase:**
   - Pros: One-liner framework, scalability, advanced features, BaaS adaptation.
   - Cons: Vendor lock, high cost.

2. **Considering alternatives like Supabase:**
   - Pros: Comparable to Firebase, lower cost, PostgreSQL usage, no vendor lock.
   - Cons: Slightly less advanced, smaller community, limited features, higher cost.

3. **Building from scratch:**
   - Pros: Full control, lightweight dependencies, full customization, low to no cost.
   - Cons: Time-consuming, potential inefficiency compared to service providers.

Looking ahead, we lean towards the second and third options to avoid future vendor lock scenarios.

The journey into backend development involves selecting a suitable database that aligns with our requirements. Criteria include real-time communication capabilities, schema alignment, global usability, scalability, and more.

Choosing the right tools is the next step, with options ranging from Raw SQL to ORM solutions like TypeORM. Compatibility, productivity, extensibility, and integration with frameworks like NestJS are crucial considerations.

The subsequent steps include defining API styles (RESTful, GraphQL, SOAP), choosing backend frameworks, leveraging tools for API development, selecting hosting solutions, establishing backend-frontend connections, and completing the backend.

A noteworthy point is that backend development extends beyond managing messaging data; it encompasses the entire system. Common API architectures include RESTful and GraphQL. Real-time communication tools like WebRTC and Socket.IO become relevant based on the case.

Additionally, we briefly touched on SAML and CIAM, which are prevalent in larger companies.

Expanding our knowledge beyond backend, we explored terms such as React Native, where libraries like Victory Native piqued our interest. Challenges with Realm SDK for Expo prompted us to consider alternative databases.

Docker's utility in backend development became apparent, offering a streamlined approach to external service integration. Exploring tools like Tauri, Electron, and NX.js to convert websites into desktop applications revealed varying strengths and weaknesses.

Finally, we learned that Next.js seamlessly supports MySQL, PostgreSQL, and MongoDB out of the box, with additional configurations possibly needed for other databases.

# V9

Firstly, as far as I recall, we encountered a new concept known as Software Architecture Design (SAD). While my understanding is still evolving, SAD seems to provide a comprehensive overview of a project. It's like a design pattern, but you could say that design patterns are a subset of software architecture design. They represent the way your project interacts in a full overview, with various types like DDD (Domain Driven Design), microservices, and more, playing a crucial role in shaping and guiding the project.

A significant part of SAD involves creating a blueprint, a practice borrowed from engineering for designing buildings. This blueprint, demonstrated through UML or other methods, illustrates the nodes, their interactions (protocols), I/O, app goals, features, and more.

SAD is typically associated with documentation, serving developers and stakeholders. The structure of this documentation varies, and it may resemble public documentation.

One specific SAD concept we explored is multi-tenancy, where a single service or a group can handle multiple tenants. Here, a tenant refers to a group of users or an individual user.

Additionally, we delved into different types of repositories such as component-based and microservices repositories. For further insights, we recommend exploring additional resources.

Our exploration extended to distributed systems, akin to cloud systems, involving nodes, servers, or computers. In simple terms, a distributed system efficiently handles tasks, especially those involving large amounts of data. Its versatility extends across various fields, earning it the moniker of "The big brother handler of hardcore tasks."

A realization dawned upon us concerning documentation. Initially dismissing it as necessary only for organizations or teams, I now see its value even for solo endeavors. Creating comprehensive documentation serves as a valuable reference covering progress, issues, blueprints, components, plans, and more. Recognizing its importance, I've decided that, before embarking on our global project, we should prioritize creating detailed documentation.

To achieve this, we explored documentation tools and frameworks. Starting with GitBook, we found it lacking in support for embedded JS or CSS code in markdown or HTML. Consequently, we shifted to Docusaurus, a tool using React with an added feature called MDX, allowing markup language within markdown files. Our tests proved it to be a promising solution, offering advanced documentation and comparisons with other tools.

Beyond documentation, we delved into the distinction between scoped packages and in-house libraries or packages. In-house libraries, often small and separate from the main repo, offer benefits such as encapsulation, abstraction, and security. Further details can be explored in additional resources.

A significant challenge we encountered involved uncovering the secrets of enterprise apps, specifically how they hide APIs. Through research and brainstorming, we identified several strategies, with options such as creating private and public repos, utilizing separate files or configurations (e.g., package.private.json), employing in-house libraries, and creating a dedicated repository for all API logic. Each strategy has its pros and cons, with our preference leaning toward options B and D for optimal results.

We also discovered that WordPress can serve as a central help website and documentation platform.

Our exploration touched on the advantages of SQLite, including its single-file database structure, simplicity, portability, and serverless nature. It dynamically allocates space based on declared needs, making it suitable for embedded systems.

We delved into the concept of MVP (Minimal Viable Product), an application showcasing the main features of the app.

We explored the term "proxy," which acts as an intermediary or server on behalf of another. Understanding proxies led us to distinguish between forward proxies (acting on behalf of clients) and reverse proxies (acting on behalf of servers). Both types can work in tandem, with forward proxies typically on the backend and reverse proxies on the frontend.

The term "application server" metaphorically referred to as the "executor" caught our attention. This server executes application code, handling HTTP and providing a local host URL as output. Notable examples include Gunicorn, uWSGI, Apache WSGI, and Nginx uWSGI.

Load balancers, software or hardware used to balance loads across different nodes (servers), also entered our exploration. We noted their integration with web servers and the variance in their use by different hosting services.

Discovering diverse APIs, such as those for search engines and documentations, emphasized the importance of .env files and the risks associated with API exposure.
