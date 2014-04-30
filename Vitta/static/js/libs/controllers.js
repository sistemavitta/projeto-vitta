

var mod = angular.module('home', ['ngCookies'])

mod.config(function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

}).run(function($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
    $http.defaults.headers.put['X-CSRFToken'] = $cookies.csrftoken;
});


function BuscarAluno($scope,$http,$window){


    $scope.ultimaPresenca= function(usuario){

        $scope.presenca = '';

        var path = '/api/presencas/'+'?username='+usuario+'&ultima=true';
        $http.get(path).success(function(data){
            // $scope.loading = false;
            $scope.presenca = data.results;
            console.log(data);
        }).error(function(data){

            console.log(data);

        });


    };



    $scope.listTreinos= function(usuario, nome){

        $scope.treinos = '';

        var path = '/api/treinos/'+usuario+'/?ultima=true';
        $http.get(path).success(function(data){
            // $scope.loading = false;
            $scope.treinos = data.treinos;
        }).error(function(data){

            console.log(data);

        });
        $scope.ultimaPresenca("robson");


    };


    $scope.atualizarPeso = function(peso, exercicio){
      $http.post('/api/peso/', {"peso": peso, "exercicio": exercicio})
      .success(function(response, status, headers, config){
        //$scope.student = response;
        console.log(status);
        notificacao('success', 'Peso Atualizado!');
      })
      .error(function(response, status, headers, config){
        //$scope.error_message = response;
        notificacao('error', 'Erro na atualização do Peso!');
        console.log(response);
      });
    };

    // $scope.trocarPeso = function(peso){
    // style="cursor: pointer;" onclick="window.location='http://google.com';"
    //     $scope.peso=peso;
    //     // if (peso ){
    //         setTimeout(function(){
    //             $window.alert(peso);
    //         }, 100)
    //     // };
    // };


    // $scope.updatePeso = function(){
    //   $http.put('/api/peso/' + 1 , {"peso": 10})
    //   .success(function(response, status, headers, config){
    //     $scope.student = response.student;
    //     $scope.enterNew = false;
    //     $scope.editing = false;
    //   })
    //   .error(function(response, status, headers, config){
    //     $scope.error_message = response.error_message;
    //   });
    // };

    $scope.buscarAluno = function(){
        if ($scope.searchText.length>0){
            $scope.usuarios = '';
            $scope.loading = true;
            $scope.informar = false;
            var path = '/api/users/?username=' + $scope.searchText;
            $http.get(path).success(function(data){
                $scope.loading = false;
                $scope.usuarios = data.results;
                notificacao('success', 'Busca realizada com sucesso!');
            }).error(function(data){
                if (data.detail == "Nenhum usuario encontrado") {
                    $scope.loading = false;
                    $scope.informar = true;
                    $scope.alerta = data.detail;
                    notificacao('information', 'Nenhum usuário encontrado!');
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
           $scope.buscarAluno();
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
