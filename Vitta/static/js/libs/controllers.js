var mod = angular.module('home', [])

 
mod.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});



mod.controller('BuscarAluno', ['$scope', function($scope,$http){

	$scope.buscar = function(){
        var path = '/talks/users/';
        $scope.loading = true;
        $.get(path).success(function(data){
            $scope.loading = false;
            $scope.usuarios = data.results;
            $scope.$digest();
        })
    };
	


}]);