

var mod = angular.module('home', [])

mod.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});


function BuscarAluno($scope,$http,$window){

    // $scope.peso=10;

    $scope.buscar = function(){
        if ($scope.searchText.length>0){
            $scope.usuarios = '';
            $scope.loading = true;
            $scope.informar = false;
            var path = '/api/users/?username=' + $scope.searchText;
            $http.get(path).success(function(data){
                $scope.loading = false;
                $scope.usuarios = data.results;
            }).error(function(data){
                if (data.detail == "Nenhum usuario encontrado") {
                    $scope.loading = false;
                    $scope.informar = true;
                    $scope.alerta = data.detail;
                } else {
                $window.alert("Erro ao buscar alunos: Verificar conexão com a internet!");
                console.log(data);
                };
            });
        }else{
            $scope.usuarios = '';
            $scope.informar = false;
        }

    };

    $scope.reset = function(){
        $scope.searchText = '';
        $scope.usuarios = '';
        $scope.informar = false;

        $('#success').on('shown.bs.modal', function () {
            $('#busca').focus();
        });

    };

    $scope.enter = function(ev){
        if (ev.which==13) {
           $scope.buscar();
        };
    };

    $scope.contem =function (list, obj, user) {
        list.push(user);
        for(var i=0; i<list.length; i++) {
            if (list[i] == obj){
                return true;
            };
        };
        return false;
    };




}
