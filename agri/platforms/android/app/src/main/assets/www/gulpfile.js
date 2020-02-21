var gulp = require("gulp");
var browserSync = require("browser-sync").create();

gulp.task("serve", function() {
  browserSync.init({
    serve: "./"
  });

  gulp.watch("./*.html").on("change", browserSync.reload);
});
