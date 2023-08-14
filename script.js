// Compile the Handlebars template
var source = document.getElementById('project-template').innerHTML
var template = Handlebars.compile(source)

Handlebars.registerHelper('isEven', function(value, options) {
  return value % 2 === 0;
});

// Render the template with the data
var html = template({ projects: projects })

// Insert the rendered HTML into the specific container
var projectContainer = document.getElementById('portfolio-projects')
projectContainer.innerHTML = html
