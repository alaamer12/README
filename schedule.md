# Schedule Structure

This file outlines the components that should be included in a comprehensive schedule.

## College Activities
- **Lectures:** Schedule timings for attending lectures.
- **Study Time:** Allocate time for reviewing lectures and completing assignments.
- **Commute:** Factor in the time spent traveling to and from college.
- **Exam Preparation:** Schedule study time leading up to exams.

## In-House Learning
- **Resource Acquisition:** Allocate time for gathering study materials.
- **Study Sessions:** Set aside time for focused studying.

## Practical Time
- **Physical Practice:** Dedicate time for physical exercises or practical demonstrations.
- **Projects:** Allocate time for working on practical projects.
- **Resource Gathering:** Schedule time to obtain necessary materials.

## Maintenance
- **Internal and External Tasks:** Allocate time for organizing and upkeep.

## Reading Time

## Leisure Time
- **Rest:** Schedule time for relaxation and rejuvenation.
- **Socializing:** Allocate time for spending with friends or family.

## Creativity
- **Schedule Creation:** Dedicate time for crafting and organizing schedules.

## Scoring System

## Management and Accounting
- **Account Setup:** Allocate time for setting up accounts.
- **Content Management:** Schedule time for creating and managing posts.
- **Interaction:** Dedicate time for engaging with content and users.

## Chatting
- **Social Interactions:** Allocate time for chatting with others, including bots.

## Ordinary Tasks
- **Daily Routine:** Schedule time for activities like sleeping, grocery shopping, and eating.

## Application Options
Deciding on the appropriate application for scheduling is crucial. Currently, two main options are under consideration: Outlook and Clockify.

### Outlook
- **Calendar Management:** Outlook excels in calendar management, offering customization options for reminders, categories, and colors.
- **Integration with OneNote:** Provides integration with OneNote for enhanced note-taking capabilities.

### Clockify
- **Task Tracking:** Clockify focuses on tracking time spent on tasks.
- **Tagging System:** Utilizes tags for organizing tasks.
- **Integration with Outlook:** Limited integration with Outlook, primarily importing calendar events without bidirectional updates.

## Decision Dilemma
Choosing between Outlook and Clockify poses a dilemma:
- **Outlook:** Offers robust calendar management but lacks extensive time tracking features.
- **Clockify:** Provides detailed task tracking but lacks customization options and seamless integration with Outlook.

### Considerations
- **Preference:** Personal preference for feature prioritization.
- **Workflow Efficiency:** Consider which application aligns better with workflow needs.
- **Manual Updates:** Recognize the need for manual updates if using both applications simultaneously.

## Conclusion
Selecting the most suitable scheduling tool requires careful consideration of individual needs and preferences. Both Outlook and Clockify offer distinct advantages, and the decision should be made based on which features are deemed most essential for effective schedule management.


---

### Notes:
- Keys marked with `<optional>` and `<no-input>` are related to implementation.

### Key Descriptions:
- **promocode:** A unique code to access the task consists of two uppercase letter e.g `CS`.
- **task name:** A fixed name for the task.
- **repeated:** Indicates how often the task is repeated (e.g., daily, weekly).
- **leaps:** Tracks the number of pauses and resumes in the task.
- **task badge:** Reflects the user's performance in the task.
- **location:** Specifies whether the task is done internally or externally.
- **deadline:** Sets a deadline three days after the due date.

### Object Keys:

#### Unique Identifiers:
- `id` <no-input>
- `promocode` <no-input>

#### Time-related:
- `creation date` <no-input>
- `update date` <no-input>
- `due date (today, yesterday, previous date)`
- `completion date (today, yesterday, previous date)`
- `deadline`
- `deadline total counter`
- `history` <no-input>

#### Task Details:
- `name`
- `description` <optional>
- `notes` <optional>
- `task name` <optional>
- `tags`
- `username` <no-input>
- `projects`
- `priority/weight of task`
- `duration` <no-input>
- `status (complete, incomplete, missed)`
- `counter of the task` <no-input>
- `counter of total leaps` <no-input>
- `leaps`
- `relation with project (strong, weak)` <optional>
- `location`
- `feedback` <optional>

#### Task Performance:
- `maximum score`
- `adherence time`
- `task completion percentage`
- `repeated`
- `obtained score (per day, week, month)` <no-input>
- `adherence rate (per day, week, month)` <no-input>
- `total maximum time (per day, week, month)` <no-input>
- `total obtained time (per day, week, month)` <no-input>
- `statistics functions (mean, stdev, var, max, mini, mode, median)` <no-input>
- `health` <optional> (unchanged, get worse, get better)
- `counter of total missing` <no-input>
- `counter of task badges` <no-input>
- `badge for total tasks` <no-input>
- `streak` <optional>
- `abondence` <no-input>
- `abondence_counter` <no-input>
- `archived` <no-input>
- `archived_counter` <no-input>
- `Task Constraints` <no-input>
