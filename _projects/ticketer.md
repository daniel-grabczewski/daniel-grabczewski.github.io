---
layout: project
in_development: 'false'
title: Ticketer
slug: ticketer
description: 'Ticketer is a visual work management platform designed to aid the way
  individuals and teams organize their tasks and projects. Utilizing the proven Kanban
  board system, Ticketer offers a seamless and intuitive interface that empowers users
  to effortlessly create, customize, and manage boards, lists, and tickets tailored
  to their unique workflows.

  '
technologies:
- Angular
- Typescript
- C#
- ASP.NET Core
- MySQL
- Azure Cloud Services
- Docker
code_url: https://github.com/daniel-grabczewski/Ticketer
demo_url: https://ticketerapp.com
key_features:
- title: Customizable Boards
  description: 'Design and organize multiple boards tailored to your projects or personal
    workflows. Personalize each board with unique names, vibrant colors, and stunning
    backgrounds to reflect your style or team identity. Easily create, save, and duplicate
    templates to streamline your setup and maintain consistency across different projects.

    '
  image: /assets/images/ticketer-project/customizable-boards.png
  caption: Screenshot of the Ticketer board page
- title: Flexible Lists
  description: 'Structure your workflow with adaptable lists that categorize your
    tasks effortlessly. Whether it''s "To Do," "In Progress," or custom categories,
    you can create, rename, and duplicate lists to build templates that fit your specific
    needs. This flexibility ensures that your task management adapts as your projects
    evolve.

    '
  image: /assets/images/ticketer-project/flexible-lists.png
  caption: Diagram showing all actions that user can perform on a list
- title: Comprehensive Tickets
  description: 'Dive deep into task management with detailed tickets. Customize each
    ticket with titles, descriptions, and cover colors for enhanced organization.
    This feature allows you to maintain both a high-level overview and granular details,
    ensuring nothing slips through the cracks.

    '
  image: /assets/images/ticketer-project/comprehensive-tickets.png
  caption: Screenshot of Ticketer's detailed ticket view
- title: Intuitive Drag-and-Drop
  description: 'Experience seamless task movement with a smooth drag-and-drop interface.
    Easily rearrange tickets within and across lists, and reorder lists themselves
    to reflect shifting priorities. This visual and interactive approach makes managing
    your tasks more engaging and efficient.

    '
  image: /assets/images/ticketer-project/intuitive-drag-and-drop.mp4
  caption: Video of using Ticketer's drag-and-drop interface
- title: Seamless Account Management
  description: 'Get started quickly by signing up with Auth0 or Google, or jump in
    as a guest to explore Ticketer without any commitments. When you''re ready to
    save your progress, effortlessly transfer your guest data to a permanent account,
    ensuring your boards are accessible from any device and securely stored in Azure''s
    cloud services for future use.

    '
  image: /assets/images/ticketer-project/seamless-account-management.png
  caption: Screenshot of the Ticketer login page
visuals:
  demo_video: https://www.loom.com/embed/d4b13274afab4d06a001c13b30f95e5e?sid=0b7e99fe-ae02-43e8-922f-435b384e931c
  dev_video: https://www.loom.com/embed/51c2dfa0c7bc4a0696bd262d7a3fb626?sid=bd87c4f6-f438-43f9-b857-a27a224548c7
  thumbnail: /assets/images/project-thumbnail.svg
development_process:
  overview: 'Developing Ticketer as a solo project was an exhilarating journey that
    pushed me to expand my technical expertise and problem-solving skills. I wanted
    to further my skills and versatility as a developer by tackling unfamiliar technologies
    such as Angular, C#, ASP.NET Core, Azure, and Docker. These technologies presented
    numerous challenges, each serving as a valuable learning opportunity. Building
    this comprehensive application from the ground up not only deepened my understanding
    of full-stack development but also reinforced the importance of meticulous planning
    and adaptability in overcoming obstacles.

    '
  steps:
  - title: Strategic Planning and MVP Definition
    description: 'The foundation of Ticketer was laid by meticulously planning out
      the Minimum Viable Product (MVP). I identified and prioritized key functionalities
      essential for a robust task management tool, ensuring that each feature aligned
      with user needs and project goals. This phase involved designing the API architecture,
      defining database schemas with clear primary keys and relationships, and outlining
      the core interactions between the frontend and backend. This strategic approach
      was crucial in setting a clear roadmap and establishing a solid base for Ticketer.

      '
    image: /assets/images/ticketer-project/mvp-outline.png
    caption: Screenshot of Ticketer MVP outline document
  - title: UI/UX Design and API Refinement
    description: 'With the MVP outlined, I transitioned to designing the user interface
      using Figma, keeping the planned APIs in mind. This alignment between UI/UX
      design and backend development allowed for a more cohesive and intuitive user
      experience. Detailed wireframes and prototypes provided a clear vision of user
      interactions, which in turn informed the refinement of API routes, parameters,
      and data models. This iterative process ensured that the APIs were not only
      functional but also optimized for seamless integration with the frontend, enhancing
      overall application efficiency.

      '
    image: /assets/images/ticketer-project/ui-ux.png
    caption: Screenshot of board page wireframe
  - title: Optimizing Data Structures for Positioning Systems
    description: 'One of the most intricate challenges was managing the dynamic positioning
      of lists and tickets within the Kanban board. Ensuring that moving a list or
      ticket seamlessly updated the positions of surrounding items required a robust
      data structure. I engineered a system where each list and ticket maintained
      a unique position index, enabling real-time updates and maintaining data integrity.
      Implementing this with ASP.NET Core and MySQL involved strategies to handle
      reordering logic efficiently, ensuring smooth and consistent user interactions
      without compromising performance.

      '
    image: /assets/images/ticketer-project/db-diagram.png
    caption: Diagram of Ticketer's database structure
  - title: Developing a Scalable Menu and Submenu System
    description: 'The heart of Ticketer''''s user interactions lies in its versatile
      menu and submenu system. To achieve a clean and reusable solution, I designed
      a dynamic configuration-based system that dictates the behavior and structure
      of all menus across the app. By creating a flexible data structure that the
      menu components could interpret, I eliminated repetitive code and facilitated
      easy scalability. This approach allowed for effortless addition of new menu
      items and submenus, ensuring consistency across the application and significantly
      reducing development time for future enhancements.

      '
    image: /assets/images/ticketer-project/scalable-menu-system.png
    caption: Diagram of the board page's menu/submenu data transfer flow
  - title: Cloud Deployment with Azure and Docker
    description: 'Deploying Ticketer on Azure using Docker containers presented a
      unique set of challenges, particularly in configuring the virtual machines and
      ensuring secure communications through SSL certificates. I navigated the complexities
      of Azure''s ecosystem by setting up automated deployment scripts, managing container
      orchestration, and configuring domain settings to establish a reliable and secure
      production environment. This hands-on experience with cloud services not only
      optimized the application''s scalability and reliability but also showcased
      my ability to manage end-to-end deployment processes effectively.

      '
    image: /assets/images/ticketer-project/azure-vm.png
    caption: Screenshot of Ticketer's Azure Virtual Machine dashboard
  - title: Outcomes and Reflections
    description: 'Ticketer stands as an example of my ability to independently manage
      and deliver a complex full-stack application. Successfully integrating Angular
      with a C# and ASP.NET Core backend, and deploying it on Azure with Docker, has
      significantly broadened my technical repertoire. The project not only operates
      seamlessly but also embodies best practices in software development, from efficient
      data structures to scalable deployment strategies. Reflecting on this journey,
      I recognize the importance of detailed planning, continuous learning, and adaptability
      in overcoming challenges, all of which have been instrumental in shaping me
      into a more proficient and resilient developer.

      '
    image: /assets/images/ticketer-project/figma-birds-eye-view.png
    caption: Birds-eye-view screenshot of Ticketer's architecture
  lessons_learned:
  - "Throughout the development of Ticketer, one of the most pivotal lessons I learned\
    \ was the importance of implementing comprehensive testing from the outset. Initially,\
    \ I underestimated the value of automated tests, believing they might slow down\
    \ development speed. I had written tests before in earlier projects, with Jest\
    \ and Vite, but I took them for granted. Because, as Ticketer grew, I encountered\
    \ multiple scenarios where the absence of tests led to elusive bugs and hindered\
    \ efficient debugging. \n"
  - 'This experience taught me the hard way that a robust testing suite is indispensable
    for maintaining code quality and reliability, especially in complex applications.
    Additionally, I gained invaluable insights into effective project management and
    time allocation, realizing that balancing feature development with thorough testing
    and documentation is essential for long-term project success.

    '
  - 'Another significant lesson was the power of leveraging cloud services effectively.
    Navigating Azure''s vast array of tools and services taught me how to optimize
    resource allocation, enhance application scalability, and ensure robust security
    measures. Managing Docker containers not only streamlined the deployment process
    but also reinforced the importance of automation in modern software development.
    These experiences have equipped me with the skills to architect scalable, secure,
    and efficient applications, making me a more versatile and capable developer.

    '
---
