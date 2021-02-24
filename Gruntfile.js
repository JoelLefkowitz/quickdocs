module.exports = function (grunt) {
    grunt.initConfig();

    grunt.registerTask("lint", [
        "cspell",
        "eslint",
        "pylint",
        "bandit",
        "mypy"
    ]);

    grunt.registerTask("format", [
        "prettier",
        "csscomb",
        "presort",
        "black",
        "autoflake",
        "isort"
    ])
}
