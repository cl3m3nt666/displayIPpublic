function GetInfoIP($scope, $http) {
    $http.get('http://ipinfo.io/json').success(function(data) {
        $scope.allinfo = data;

    });
}
