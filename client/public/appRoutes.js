angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'retails',
        url: '/',
        templateUrl: 'public/components/retails/templates/retails.template',
        controller: 'RetailController'
    });

    $urlRouterProvider.otherwise('/');
}]);