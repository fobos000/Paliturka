

var my_app = angular.module('Book', ['ngCookies'])
    .run( function run( $http, $cookies ){

    // For CSRF token compatibility with Django

    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
})
    .config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

});

my_app.controller('Post_Controller', function($scope, $http) {
    $scope.submit = function() {
        var in_data = { subject: $scope.subject };
        $http.post('/new_book', in_data)
            .success(function(out_data) {
                // do something
            });
    }
});