---
layout: project
in_development: 'false'
title: Boba Business Management
slug: boba-business-management
description: 'Boba Business Management, a team project, is a comprehensive platform
  for simulating an online bubble tea business. Every time you open the app, you''ll
  be greeted with new orders to manage, reviews to moderate, emails to read, and products
  to restock. You can switch between Admin and Shopper modes at any time, and every
  action you take in one mode directly affects the other.

  '
technologies:
- React
- TypeScript
- SQLite
- Jest
- Auth0
- Tailwind CSS
code_url: https://github.com/daniel-grabczewski/boba-business-management
demo_url: https://daniel-grabczewski.github.io/boba-business-management/admin
key_features:
- title: Dashboard Overview
  description: 'Monitor your store''s health at a glance with an intuitive dashboard
    that highlights new orders, product stock levels, recent reviews, and incoming
    messages requiring attention. This streamlined overview keeps you informed about
    critical updates, helping you make quick decisions that drive business performance.
    Stay one step ahead with real-time alerts and concise, actionable insights.

    '
  image: /assets/images/bbm-project/dashboard.png
  caption: Screenshot of the admin dashboard
- title: Comprehensive Management Pages
  description: 'Take charge of your online store with dedicated pages for emails,
    orders, reviews, and products. Each page offers advanced searching, filtering,
    sorting, and pagination, ensuring you can swiftly locate the details you need.
    Drill down into any item for a closer look, then moderate, respond, or update
    information with ease.

    '
  image: /assets/images/bbm-project/comprehensive-management.mp4
  caption: Video of interacting with admin pages
- title: Product Creation & Modification
  description: 'Easily build and update your product catalog with detailed entries
    for name, description, price, stock levels, and images. Make real-time edits to
    reflect changes in inventory or promotional pricing, ensuring customers always
    see accurate information. Keep your listings appealing and competitive by refining
    product details whenever necessary for maximum engagement.

    '
  image: /assets/images/bbm-project/product-modification.png
  caption: Screenshot of the edit-product page
- title: Dual-Role Experience
  description: 'Effortlessly toggle between Shopper and Admin perspectives to explore
    your store from every angle. In Shopper mode, browse products, fill carts, and
    leave reviews, while Admin mode handles stock management, order processing, and
    content moderation. Any action in one role instantly affects the other, creating
    a seamless, real-time feedback loop.

    '
  image: /assets/images/bbm-project/dual-role-experience.mp4
  caption: Video of switching to shopper view and buying products
- title: Self-Contained Shopper Environment
  description: 'Enhance the user journey with a realized shopper environment that
    goes beyond basic browsing.  Shoppers can view and manage orders in a personalized
    profile, keep a wishlist, and edit personal  details like addresses or phone numbers.
    They can also leave product reviews to share feedback,  creating a vibrant shopping
    experience.

    '
  image: /assets/images/bbm-project/profile-page.png
  caption: Screenshot of the shopper user's profile page
visuals:
  demo_video: https://www.loom.com/embed/d7ee2e9357a14fbab558146a4312a016?sid=99afbb39-59e4-4275-a393-5a41db15d92e
  dev_video: https://www.loom.com/embed/49f11b502ea44106b513c20ec25f087b?sid=b5e50c31-67b2-49ee-bf37-8a4c612fc501
  thumbnail: /assets/images/project-thumbnail.svg
development_process:
  overview: 'Our main objective with Boba Business Management was to create a robust,
    feature-complete application  that showcased everything we had learned during
    our intensive coding bootcamp. We incorporated a  familiar tech stack (React,
    TypeScript, Express, SQLite, and Auth0) while maintaining a systematic  approach
    from the start. By committing to Agile methods, thorough planning, and consistent
    communication,  we tackled complex features like dual-role functionality and daily
    data generation, infusing a realistic  simulation layer into the standard e-commerce
    environment.

    '
  steps:
  - title: Planning the App
    description: 'We started by defining a vision that balanced shopper interactions
      with admin oversight for a  two-in-one store simulation. Detailed feature lists
      and user stories kept both sides aligned,  covering real-time stock updates,
      user reviews, and daily notifications. Once core capabilities  were agreed upon,
      we mapped out our APIs and database schema to anticipate potential bottlenecks.  This
      systematic approach clarified how the front end and back end would interact,
      saving us from  guesswork and streamlining development.

      '
    image: /assets/images/bbm-project/planning.png
    caption: Screenshot of a portion of API plans for planned features
  - title: Developing the Wireframe
    description: 'We transitioned to Figma to wireframe our interfaces collaboratively,
      making live edits to layout,  navigation flow, and user experience. By mapping
      features and components visually, we reduced the  risk of missing essential
      elements during coding. This phase also sparked discussions about color  palettes,
      branding, and displaying data like product inventories. Ultimately, wireframing
      aligned  our visual goals and user pathways before any code was written, enabling
      a smoother transition into  development.

      '
    image: /assets/images/bbm-project/wireframe.png
    caption: Screenshot of some wireframes from Figma
  - title: Working Effectively as a Team
    description: 'After finalizing wireframes, we adopted an Agile workflow with daily
      standups to address progress  and obstacles. End-of-day retrospectives highlighted
      wins and areas to refine, keeping morale high  and processes agile. Communication
      thrived in our shared Discord channel, where we quickly tackled  code reviews,
      bug fixes, and urgent questions. This continuous feedback loop ensured issues
      were  resolved before escalating, and everyone felt accountable for the project''s
      success. Collaborative  ownership and transparency became the foundation of
      our productivity.

      '
    image: /assets/images/bbm-project/discord.png
    caption: Screenshot of our team's shared Discord channel
  - title: Organization & Task Delegation
    description: 'We used Trello to break down each feature into actionable tickets,
      linking them to relevant  wireframes and APIs. Every ticket included clear objectives,
      acceptance criteria, and any  dependencies, so teammates understood their responsibilities.
      Pull-request duties rotated,  providing collective experience in code review,
      version control, and integration testing.  By merging frequently, we prevented
      major conflicts, ensuring the codebase remained stable.  Transparent deadlines
      and straightforward workflows allowed team members to focus on tasks  while
      keeping sight of overall progress.

      '
    image: /assets/images/bbm-project/trello-board.png
    caption: Screenshot of delegated tasks on our team's Trello board
  - title: Ensuring Secure Routes
    description: 'We needed a robust security model to protect admin-only pages, so
      we integrated Auth0 for  authentication and a custom layer to verify admin status
      in our database. This prevented  unauthorized changes that could alter product
      listings, override pricing, or disable items.  Each request was scrutinized,
      ensuring users had proper credentials to perform high-level  actions. Rigorous
      testing and peer reviews helped us identify gaps, reinforcing data integrity  and
      user trust across all sensitive operations.

      '
    image: /assets/images/bbm-project/secure-routes.png
    caption: Screenshot of our Admin authorization wrapper
  - title: Enhancing It Further on My Own
    description: 'Some months later, I expanded the project "Boba Buddies" into "Boba
      Business Management," focusing on realism  and user immersion. Randomized daily
      orders, reviews, and messages added unpredictability,  prompting vigilant stock
      monitoring and review moderation. Query parameters preserved filters,  sorts,
      and searches, addressing a major pain point from the original version. I removed
      the strict authentication, so users could easily switch roles, creating a smoother
      demo experience. If you would like to experience the admin authentication, it
      is still available in the original Boba Buddies.

      '
    image: /assets/images/bbm-project/db-diagram.png
    caption: Diagram of BBM's modified database structure to enable new features
    bbm-readme_link: https://github.com/daniel-grabczewski/boba-business-management/blob/main/README.md
    bbm-original_project_link: https://github.com/Boba-Buddies/boba-buddies-store
  - title: Outcomes & Reflections
    description: 'Boba Business Management successfully demonstrated our full-stack
      expertise and adaptability,  moving seamlessly between shopper and admin views.
      Our methodical process—roadmapping,  wireframing, implementing Agile ceremonies,
      and rigorous testing—proved that structured  planning leads to smoother development
      cycles. Personally, I learned to balance user  convenience against real-world
      complexity. This experience illuminated the importance of  collaborative teamwork,
      thoughtful design, and ongoing refinement in delivering a robust,  future-proof
      application that truly meets users'' needs. It also solidified my confidence  in
      managing large-scale project coordination.

      '
    image: /assets/images/bbm-project/figma-birds-eye-view.png
    caption: Birds-eye-view screenshot of BBM's architecture
  lessons_learned:
  - 'Collaboration can be challenging when balancing different schedules and working
    styles, but our daily standups and open communication channels were vital for
    resolving conflicts. We learned that consistent team check-ins create a culture
    of support and shared progress.

    '
  - 'Detailed planning prevents feature overload. Initially, too many ideas floated
    around without a solid anchor, risking a chaotic development process. Creating
    an agreed-upon roadmap, aligning features with APIs, and sticking to defined milestones
    allowed us to deliver a polished, cohesive product.

    '
  - 'Personally, I learned the value of taking ownership. By spearheading the upgraded
    version, “Boba Business Management,” I improved my skills in dynamic feature development,
    mobile-responsive design, and UI/UX enhancements. This experience solidified my
    confidence as both a contributor and a solo developer.

    '
---
