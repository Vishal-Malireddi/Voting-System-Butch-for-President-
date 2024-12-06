# Sprint 3 Report (11/5/2024 - 12/05/2024)

## Sprint Video


## What's New (User Facing)

Regarding user facing additions, we have added some new inputs for the node pallete, as well as adding a candidate, job posting and analaytics page.  In the node pallete we changed
the nodes for both the email, phone and automation nodes which should make it easier for a user to view.  For the candidate queue, the user will be able to see all candidates associated
with their organization, as well as their respective information.  For the job posting page, the user will be able to view all jobs that are associated to their organization as well as being able
to use a searchable dropdown menu to assign any node flow to a job.  There is also now an analytics page, which doesnt display any information, but it does exist.  Finally we added a login and 
authentification system for users.

## Work Summary (Developer Facing)

First we developed a backend for the candidate queue.  This uses a Tanstack Querry to access the Cosmos DB, from there the candidates queue page is dynamically populated with the information.
We also added a similar system to the job postings page.  A Tanstack Querry is used to acces the DB, and the page is then dynamically populated.  However, another querry is then used to access the available
flows and populate a dynamically searchable dropdown menu containing the node flows.  We also have deployed the application to Azure, as well set up an Azure Service Bus in order to assist the candidate queue.

## Unfinished Work

Ultimately, we still need to finish the action functionality for the job posting page.  Currently the frontend aspects of the page are completed however, we still need to add functionality to the button which 
should assign all candidates associate to a job to the relative node flow.  For the analytics page, we also need to finish the functionlity of the backend, as currently it just displays some hard coded 
values that arent associated with the account.  Finally, we also need to start working on the node processing engine.

## Completed Issues/User Stories
Here are links to the issues that we completed in this sprint:

 * https://github.com/Symbal-AI/recruiter-tree/issues/51
 * https://github.com/Symbal-AI/recruiter-tree/issues/55
 * https://github.com/Symbal-AI/recruiter-tree/issues/56
 * https://github.com/Symbal-AI/recruiter-tree/issues/57
 * https://github.com/Symbal-AI/recruiter-tree/issues/59
 * https://github.com/Symbal-AI/recruiter-tree/issues/61
 * https://github.com/Symbal-AI/recruiter-tree/issues/63
 * https://github.com/Symbal-AI/recruiter-tree/issues/65
 * https://github.com/Symbal-AI/recruiter-tree/issues/68
 * https://github.com/Symbal-AI/recruiter-tree/issues/72
 * https://github.com/Symbal-AI/recruiter-tree/issues/73
 * https://github.com/Symbal-AI/recruiter-tree/issues/79
 * https://github.com/Symbal-AI/recruiter-tree/issues/81

## Incomplete Issues/User Stories
Here are links to issues we worked on but did not complete in this sprint:
 * https://github.com/Symbal-AI/recruiter-tree/issues/69 (Lots of issues in making sure it's stable)
 * https://github.com/Symbal-AI/recruiter-tree/issues/54 (Pushing to next sprint)
 * https://github.com/Symbal-AI/recruiter-tree/issues/53 (Pushing to next sprint)
 * https://github.com/Symbal-AI/recruiter-tree/issues/52 (Pushing to next sprint)
 * https://github.com/Symbal-AI/recruiter-tree/issues/50 (Pushing to next sprint)
 * https://github.com/Symbal-AI/recruiter-tree/issues/49 (Pushing to next sprint)
 * https://github.com/Symbal-AI/recruiter-tree/issues/28 (Lots of issues in making sure it's stable)

## Code Files for Review
Please review the following code files, which were actively developed during this sprint, for quality:

**Note: all files here are carried over from another project, but were quality reviewed**
- Symbal-AI/recruiter-tree/frontend/docker-compose.yml
- Symbal-AI/recruiter-tree/frontend/Dockerfile
- Symbal-AI/recruiter-tree/frontend/src/
   - reportWebVitals.ts
   - index.tsx
   - Flow.tsx
   - app/slices
   - app/slices/colorModeSlice.ts
   - app/slices/copyPasteSlice.ts
   - app/slices/editorSlice.ts
   - app/slices/flowSlice.ts
   - app/slices/inputOutputSlice.ts
   - app/flowLayout.ts
   - app/store.ts
   - editor/modals
   - editor/modals/ConfirmModal.tsx
   - editor/ColorPicker.tsx
   - editor/MenuBar.tsx
   - editor/SearchPopup.tsx
   - nodes/CandidateEntry.tsx
   - nodes/FunctionCallNode.tsx
   - nodes/FunctionOutput.tsx
   - nodes/NodeWrapper.tsx
      
## Retrospective Summary
Here's what went well:
  * Not too much tbh
 
Here's what we'd like to improve:
   * So much
  
Here are changes we plan to implement in the next sprint:
   * Become 10x developers
