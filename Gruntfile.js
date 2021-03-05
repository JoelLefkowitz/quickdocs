function quit(name) {
  console.log("Task: '".concat(name, "' has not been implemented"));
}
module.exports = function (grunt) {
  grunt.initConfig({
    exec: {
      lint: "pylint",
      testsUnit: "tox",
      testsCoverage: "pytest --cov=quickdocs tests/",
      docsBuild: "sphinx-build docs build"
    }
  });
  grunt.loadNpmTasks('grunt-exec')
  grunt.registerTask("lint", "exec:lint");
  grunt.registerTask("tests:unit", "exec:testUnit");
  grunt.registerTask("tests:coverage", "exec:testCoverage");
  grunt.registerTask("docs:build", "exec:docsBuild");
};
