module.exports = function(grunt) {

    // loosely following: https://24ways.org/2013/grunt-is-not-weird-and-hard/

    // Project configuration
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
    
        // "Configuration for concatinating files"
        concat: {   
            js: {
                src: [	'node_modules/jquery/dist/jquery.js',
			'node_modules/bootstrap/dist/js/bootstrap.js',
			'node_modules/qtip2/dist/jquery.qtip.js',
			'custom/js/custom.js',
                     ],
                dest: 'build/production.js',
            },
            css: {
                src: [  'vendor/css/bootstrap-3.3.4-dist.css',
                        'vendor/css/carousel.css',
                        // 'node_modules/bootstrap/dist/css/bootstrap-theme.min.css',
                        // 'node_modules/bootstrap/dist/css/bootstrap.min.css',
                        // 'node_modules/qtip2/dist/jquery.qtip.min.css',
                        // 'node_modules/hover.css/css/hover-min.css',
                        'custom/css/*.css',
                     ],
                dest: 'build/production.css',
            }
        },
        // uglify = minify
        uglify: {
            options: {
                banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
            },
            build: {
                src: 'build/production.js',
                dest: 'build/production.min.js'
            }
        }
    });
    
    // Load the plugin that provides the "uglify" task.
    // "Where we tell Grunt we plan to use this plug-in"
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-concat');
    
    // Default task(s).
    // "Where we tell Grunt what to do when we type 'grunt' into the terminal."
    grunt.registerTask('default', ['concat', 'uglify']);

};
