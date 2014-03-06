

var mod = angular.module('home', [])

mod.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});


function BuscarAluno($scope,$http){



    $scope.buscar = function(){
        var path = '/talks/users/';
        $http.get(path).success(function(data){
            $scope.usuarios = data.results;
        }).error(function(data){
            alert("Erro ao buscar alunos");
            console.log(data);
        });
    };

}