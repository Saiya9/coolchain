var app = angular.module('plunker', []);

app.filter('parseDate', function () {
        return function (date) {
          if (angular.isDate(date)) return date;
          return new Date(Date.parse(date.replace(/:\d{2}[.,]\d{3}Z$/, '')));
        };
    });

app.controller('MainCtrl', function($scope, $filter) {
  $scope.name = 'World';
  
  var ship_time = "2017-08-29T17:15:16.814Z";
  
  $scope.start_date = $filter('parseDate')(ship_time);
});
