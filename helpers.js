function getProjectDetails(projectName) {
  return projects.find((project) => project.name === projectName)
}

function loadAndRenderProject(projectName) {
  const projectDetails = getProjectDetails(projectName)
  if (!projectDetails) {
    console.error('Project not found')
    return
  }

  fetch('../project-info-template.hbs')
    .then((response) => response.text())
    .then((templateStr) => {
      const template = Handlebars.compile(templateStr)
      const html = template(projectDetails)
      document.body.innerHTML += html
    })
    .catch((error) => console.error('Error loading the template:', error))
}
