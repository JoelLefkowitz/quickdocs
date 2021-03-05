function quit(name) {
  console.log("Task: '".concat(name, "' has not been implemented"));
}
module.exports = function (grunt) {
  grunt.initConfig({
    exec: {
      lint: "echo \"Lint not implemented\"",
      testsUnit: "tox",
      testsCoverage: "pytest --cov=quickdocs tests/ --cov-report=xml:cov.xml",
      docsBuild: "sphinx-build docs build",
    },
  });
  grunt.loadNpmTasks("grunt-exec");
  grunt.registerTask("lint", "exec:lint");
  grunt.registerTask("tests:unit", "exec:testsUnit");
  grunt.registerTask("tests:coverage", "exec:testsCoverage");
  grunt.registerTask("docs:build", "exec:docsBuild");
};
