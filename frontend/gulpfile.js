var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var watch = require('gulp-watch');
var uglifycss = require('gulp-uglifycss');

gulp.task('js', function() {
    return gulp.src('js/**/*.js')
        .pipe(concat('main.js'))
        .pipe(gulp.dest('dist/js'));
});

gulp.task('css', function() {
    return gulp.src([
        "bower_components/bootstrap/dist/css/bootstrap.min.css",
        "bower_components/bootstrap-datepicker/dist/css/bootstrap-datepicker.min.css",
        "bower_components/angular-datepicker/dist/angular-datepicker.min.css",
        "css/main.css"])
        .pipe(concat('main.css'))
        .pipe(gulp.dest('dist/css'));
});

gulp.task('vendor_js', function() {
    return gulp.src([
        "bower_components/jquery/dist/jquery.min.js",
        "bower_components/bootstrap/dist/js/bootstrap.min.js",
        "bower_components/angular/angular.min.js",
        "bower_components/angular-route/angular-route.min.js",
        "bower_components/moment/min/moment.min.js",
        "bower_components/angular-datepicker/dist/angular-datepicker.min.js",
        "bower_components/angular-md/dist/angular-md.min.js",
        "bower_components/marked/lib/marked.js",
        "bower_components/lodash/dist/lodash.min.js"
        ])
        .pipe(concat('vendor.js'))
        .pipe(gulp.dest('dist/js'));
});

gulp.task('fonts', function() {
    return gulp.src(['bower_components/bootstrap/dist/fonts/*'])
        .pipe(gulp.dest('dist/fonts'));
});

gulp.task('pages', function() {
    return gulp.src('pages/*')
        .pipe(gulp.dest('dist/pages'));
});

gulp.watch('js/**/*.js',  ['js']);
gulp.watch('css/**/*.js', ['css']);

gulp.task('default', ['js', 'vendor_js', 'pages', 'css', 'fonts'])
