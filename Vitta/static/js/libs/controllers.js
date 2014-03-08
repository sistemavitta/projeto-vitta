

var mod = angular.module('home', [])

mod.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});


function BuscarAluno($scope,$http,$window){



    $scope.buscar = function(){
        $scope.searchText = ''
        $scope.usuarios = '';
        $scope.loading = true;
        var path = '/api/users/';
        $http.get(path).success(function(data){
            $scope.loading = false;
            $scope.usuarios = data.results;
        }).error(function(data){            
            $window.alert("Erro ao buscar alunos");
            console.log(data);
        });
    };

}