var mod = angular.module('home', [])

function BuscarAluno($scope){



  $scope.buscar = function(){
        var path = 'http://vitta.herokuapp.com/talks/users/';
        $scope.loading = true;
        $.get(path).success(function(data){
            $scope.loading = false;
            $scope.usuarios = data.results;
            $scope.$digest()
        });
    };

}