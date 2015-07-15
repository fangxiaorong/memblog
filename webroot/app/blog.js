define(['plugins/router'], function (router) {
    return {
        router: router,
        activate: function () {
            return router.map([
                { route: ['', 'home'],                 moduleId: 'home/index',           title: 'Home',         nav: true },
                { route: 'articles',                   moduleId: 'articles/index',       title: 'Article',      nav: true },
                { route: 'about',                      moduleId: 'about/index',          title: 'About',        nav: true },
                { route: 'github',                     moduleId: 'github/index',         title: 'Github',       nav: true },
                { route: 'article/:id',                moduleId: 'article/index',        title: 'Article',      nav: false }
            ]).buildNavigationModel()
              .mapUnknownRoutes('505/index', 'not-found')
              .activate();//({hashChange: true, pushState: true});
        }
    };
});
