module.exports = function (grunt) {
  grunt.initConfig({
    exec: {
      bandit: "bandit -c .bandit -r quickdocs", 
      cspell: "npx cspell -c .cspell.json '{*,.*,**/*}'",
      mypy: "mypy quickdocs",
      pylint: "pylint --rcfile .pylintrc quickdocs",
      quickdocs: "quickdocs .quickdocs.yml",
      remark: "npx remark -r .remarkrc .",
      sphinx: "sphinx-build docs build",
      tox: "tox",
    },
  });

  grunt.loadNpmTasks("grunt-exec");

  grunt.registerTask("lint", [
    "exec:cspell",
    "exec:remark",
    "exec:pylint",
    "exec:bandit",
    "exec:mypy",
  ]);

  grunt.registerTask("tests:unit", "exec:tox");
  grunt.registerTask("docs:generate", "exec:quickdocs");
  grunt.registerTask("docs:build", "exec:sphinx");
  grunt.registerTask("precommit", ["lint", "tests:unit", "docs:generate"]);
};
