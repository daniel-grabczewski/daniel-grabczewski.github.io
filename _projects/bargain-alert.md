---
layout: project
in_development: 'true'
title: Bargain Alert
slug: bargain-alert
description: 'Bargain Alert is an app in development that is designed to improve how
  users discover and act on incredible deals. Approved to access TradeMe''s official
  APIs, it empowers users with real-time, personalized notifications tailored to their
  exact preferences. With features that go beyond TradeMe''s native services, Bargain
  Alert ensures users never miss a deal by offering unmatched flexibility, speed,
  and precision in managing their search criteria. Whether you''re a casual bargain
  hunter or a seasoned deal enthusiast, Bargain Alert is your ultimate tool for securing
  the best deals—on the go, any time, anywhere.

  '
technologies:
- React
- Typescript
- C#
- ASP.NET Core
- PostgreSQL
- SendGrid
- Azure Cloud Services
- Docker
code_url: ''
demo_url: ''
key_features:
- title: Who is Bargain Hunter for?
  description: 'Bargain Alert is for users who want to find the best deals on TradeMe
    without constantly refreshing pages or manually checking for updates. While TradeMe
    offers a daily notification system, it''s far too infrequent to compete for top-tier
    deals in real time. This app is built for those who demand instant updates, ensuring
    they can act immediately on new listings that match their preferences. Additionally,
    Bargain Alert is designed with a mobile-first UI, recognizing that deal hunting
    often happens on the go. Whether you''re commuting, shopping, or simply managing
    your day, this app will seamlessly fit into your busy lifestyle.

    '
  image: /assets/images/bargain-hunter-project/notification-page.svg
  caption: Design for Bargain Hunter's listing notifications page
- title: Exclusive features not found on TradeMe
  use_bullet_points: 'true'
  description: 'Bargain Alert offers a host of unique and advanced features that go
    beyond what TradeMe currently provides. These features are crafted to make your
    search highly efficient and personalized, saving you time while increasing the
    likelihood of finding listings that truly matter. Beyond providing faster notifications,
    Bargain Alert introduces intelligent search capabilities designed to deliver highly
    relevant results.

    '
  bullet_points:
  - Search items across multiple categories simultaneously
  - Customizable keywords (must-have, desired, and avoid)
  - Advanced Boolean search logic
  - Filter by minimum seller rating
  - Seller proximity within a custom radius
  - Personalized relevance scoring for listings
  - Live updates for new comments on listings of interest
  image: /assets/images/bargain-hunter-project/bargain-hunter-auto-search.svg
  caption: Design for Bargain Hunter's auto-search page
- title: Why I'm building this app
  description: "Building Bargain Alert is a pivotal step in my journey as a software\
    \ developer, offering an opportunity to deepen my expertise while expanding into\
    \ new territories. While I have prior experience integrating external APIs, this\
    \ project represents the first time I'll be working with official APIs that require\
    \ application approval. Navigating the compliance requirements, terms of service,\
    \ and developer guidelines is a monumental learning experience that strengthens\
    \ my understanding of building enterprise-grade applications. \n"
  image: /assets/images/bargain-hunter-project/home-page.svg
  caption: Design for Bargain Hunter's home page
- title: Improving my technical knowledge
  description: 'Apart from learning how to work with offical APIs, I am leveraging
    this project to further enhance my skills in technologies I''m already proficient
    with, such as React and ASP.NET Core, while mastering new ones like PostgreSQL
    and SendGrid. The opportunity to explore these tools in a real-world context ensures
    I remain at the forefront of modern development practices. For me, every project
    is a chance to grow, innovate, and refine my craft. And Bargain Alert is no exception!

    '
  image: /assets/images/bargain-hunter-project/stack-diagram.svg
  caption: Architecture diagram for Bargain Hunter's technologies
choice_of_technologies:
  overview: 'Selecting the right tech stack for Bargain Alert was a meticulous process,
    grounded in research and careful consideration of the app''s requirements. Each
    technology was chosen to complement the others, ensuring a seamless, scalable,
    and high-performing system. My decision-making process focused on balancing developer
    productivity, long-term maintainability, and the specific needs of the app, such
    as real-time notifications, structured and semi-structured data handling, and
    a mobile-first experience. This thoughtful approach demonstrates not only my technical
    expertise but also my ability to align technical solutions with business objectives.

    '
  technologies:
  - title: 'Frontend Development: React & Typescript'
    description: 'React and Typescript were chosen for the frontend due to their proven
      track record in building scalable and dynamic user interfaces. React''s component-based
      architecture allows for efficient development and reusability, which is crucial
      for creating a responsive, mobile-first UI like Bargain Alert. Typescript enhances
      this process by adding type safety, reducing runtime errors, and improving developer
      confidence through better tooling and autocompletion. Together, they provide
      a modern and robust foundation for delivering a polished and user-friendly experience.

      '
  - title: 'Backend Development: ASP.NET Core & PostgreSQL'
    description: 'ASP.NET Core is an excellent choice for the backend due to its high
      performance, cross-platform support, and strong integration with C#. Its ability
      to handle concurrent requests efficiently ensures the app can scale as user
      demand increases. PostgreSQL was selected as the database because of its versatility
      and advanced features, such as JSONB support. This makes it ideal for handling
      semi-structured data like notification payloads while still offering robust
      relational capabilities for managing structured user data. Together, ASP.NET
      Core and PostgreSQL create a reliable and scalable backend infrastructure tailored
      to Bargain Alert''s needs.

      '
  - title: 'Cloud Services & Email Delivery: Azure & SendGrid'
    description: 'Azure Cloud Services was chosen for its seamless integration with
      ASP.NET Core and PostgreSQL, as well as its scalability. Azure provides reliable
      hosting and services that ensure the app performs optimally under varying workloads.
      SendGrid was selected as the email notification provider due to its effortless
      integration with Azure and its reputation for delivering secure and reliable
      email services. This combination guarantees that users receive timely and consistent
      notifications, a critical feature for Bargain Alert''s success.

      '
  - title: 'Containerization: Docker'
    description: 'Docker was chosen to streamline development and deployment by providing
      a consistent environment across all stages of the development lifecycle. With
      Docker, the app can be easily containerized, ensuring that dependencies and
      configurations are packaged together. This approach minimizes compatibility
      issues and simplifies scaling, especially as the app transitions from development
      to production. Docker''s portability and efficiency make it an essential tool
      for maintaining high-quality deployment practices in modern web development.

      '
development_process:
  overview: 'The development journey of Bargain Alert follows the structured 7-step
    Software Development Life Cycle (SDLC). This approach ensures a methodical progression
    from concept to delivery, focusing on quality, scalability, and maintainability
    at each phase. The process includes clear timelines, defined goals, and actionable
    milestones, providing a roadmap to successfully deliver a high-performing and
    user-centric application.

    '
  steps:
  - title: 'Phase 1: Planning & Requirement Analysis'
    description:
    - "The planning phase focuses on defining the project scope, setting objectives,\
      \ and resource allocation. For Bargain Alert, this involves identifying the\
      \ key problem—providing users with real-time notifications for personalized\
      \ TradeMe deals—and setting clear goals for the app's functionality and user\
      \ experience. \n"
    - 'Resource planning has included choosing a tech stack that aligns with the app''s
      requirements, such as PostgreSQL for semi-structured notification data and Azure
      for scalability. Additionally, I''ve created a project timeline to ensure steady
      progress while maintaining flexibility to adapt to new insights during development.

      '
  - title: 'Phase 2: Defining Requirements'
    description:
    - 'In this phase, requirements are being refined by gathering feedback from real
      users of TradeMe. While I don''t have official stakeholders, I''ve reached out
      to friends and colleagues who frequently use TradeMe to understand their pain
      points and desired features. Their input has been invaluable in shaping the
      app''s core functionalities, such as customizable search filters, real-time
      notifications, and a mobile-first design.

      '
    - 'By combining user insights with a strong understanding of TradeMe''s existing
      features, I''m able to define detailed user stories and feature sets that directly
      address the needs of my target audience.

      '
  - title: 'Phase 3: Design (Current phase)'
    description:
    - "At this stage, I am focusing on translating requirements into concrete designs.\
      \ I've completed the UI mockups, emphasizing simplicity and responsiveness for\
      \ a seamless mobile-first experience. \n"
    - 'Concurrently, I''m planning the database schema to efficiently handle both
      structured user data and semi-structured notification payloads. API design is
      also in progress, detailing endpoints and communication logic for retrieving
      and storing data. Additionally, I am designing the React components to ensure
      modularity and maintainability in the frontend, aligning every aspect with the
      app''s overarching goals.

      '
  - title: 'Phase 4: Development'
    description:
    - 'In the development phase, I will begin implementing the app based on the designs
      and requirements. This includes building the frontend with React and Typescript,
      ensuring a smooth user experience with reusable components, and implementing
      the backend with ASP.NET Core to handle business logic and API endpoints.

      '
    - 'PostgreSQL will be integrated to manage user data and notification storage,
      leveraging JSONB for flexibility in handling semi-structured data. Continuous
      integration tools will be used to ensure code quality and streamline deployments.
      The focus during this phase will be on creating a solid, functional MVP while
      adhering to clean coding practices.

      '
  - title: 'Phase 5: Testing'
    description:
    - 'Testing is a critical phase where I will rigorously evaluate the app''s performance,
      functionality, and reliability. This includes writing unit tests, integration
      tests, and end-to-end tests to cover all aspects of the application. I will
      also implement automated testing pipelines to ensure efficiency.

      '
    - 'From my previous project, Ticketer, I learned the importance of dedicating
      significant time to testing. In that project, I prioritized speed over thorough
      testing, which led to issues during deployment. For Bargain Alert, I am committed
      to ensuring every feature is robust, with ample time allocated to identify and
      fix potential bugs before release.

      '
  - title: 'Phase 6: Deployment'
    description:
    - "Deployment will involve launching the app on Azure Cloud Services, leveraging\
      \ its scalability and reliability for hosting both the frontend and backend.\
      \ I will use Docker to containerize the application, ensuring consistency across\
      \ environments and simplifying the deployment process. \n"
    - 'The deployment process will also include setting up monitoring tools to track
      the app''s performance and identify any issues post-launch. Ensuring a smooth
      deployment is key to delivering a professional and seamless user experience.

      '
  - title: 'Phase 7: Maintenance'
    description:
    - 'The maintenance phase focuses on continuously improving the app based on user
      feedback and performance metrics. I plan to gather insights from friends and
      early adopters testing the app, allowing me to identify bugs, usability issues,
      and potential new features.

      '
    - 'Regular updates will be deployed to address these findings, ensuring the app
      remains functional and relevant. I will also monitor API usage, email delivery
      rates via SendGrid, and other key metrics to maintain optimal performance. Adhering
      to best practices, this phase ensures Bargain Alert evolves to meet user needs
      over time.

      '
anticipated_challenges:
  overview: 'Every app comes with its own set of challenges, but Bargain Alert introduces
    new complexities for me as a developer. From building a robust and scalable email
    notification system to adhering to official API guidelines, this project pushes
    me into uncharted territory. These challenges provide an exciting opportunity
    to expand my skill set and demonstrate my ability to tackle advanced problems
    with thoughtful and effective solutions.

    '
  challenges:
  - title: Building a scalable notification system
    description: 'One significant anticipated challenge is ensuring the app''s notification
      system remains efficient and scalable as the user base grows. With notifications
      potentially being sent every five minutes and customized for each user''s criteria,
      there''s a risk of overwhelming the system, particularly as the database grows
      larger and the number of simultaneous users increases. To tackle this, I plan
      to implement a queue-based messaging system, such as Azure Service Bus, to manage
      email notifications efficiently. By decoupling the notification generation process
      from the main application flow, I can ensure consistent performance and prevent
      bottlenecks. Additionally, optimizing database queries and leveraging PostgreSQL''s
      JSONB indexing will allow for fast retrieval of complex user criteria.

      '
  - title: Handling the exclusive features
    description: 'Another anticipated challenge is handling the complex search filters
      and criteria defined by users. Features like multi-category searches, proximity-based
      seller filtering, and advanced Boolean logic require intricate database queries
      that can quickly become computationally expensive. To address this, I plan to
      use a combination of stored procedures and materialized views in PostgreSQL
      to precompute and cache commonly used queries. This will significantly reduce
      processing time and allow the app to deliver real-time results without compromising
      performance.

      '
  - title: Precisely following TradeMe's API guidelines at every step
    description: 'A third challenge lies in ensuring robust API integration with TradeMe''s
      official APIs, which involves complying with their strict terms of service and
      handling potential API rate limits. Since notifications rely heavily on frequent
      API calls, managing these limits while maintaining real-time functionality will
      be crucial. To overcome this, I plan to implement caching mechanisms to store
      recent API results and avoid redundant calls. Additionally, I''ll build a dynamic
      scheduling system that optimally spaces API requests based on user activity
      and TradeMe''s rate limits. This ensures compliance with their guidelines while
      delivering timely updates to users.

      '
---
