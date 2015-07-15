define(['durandal/app', 'durandal/system', 'knockout', 'plugins/http', 'marked', 'config'], function (app, system, ko, http, marked, config) {
    return {
        articles: ko.observableArray([]),
        activate: function() {
            system.log('Lifecycle : activate : hello');
            var that = this;

            qs = {};
            return http.get(config.base_url + "article/list", qs).then(function(response) {
                for (var idx = 0; idx < response.articles.length; idx ++) {
                    var article = response.articles[idx];
                    article.content = marked(article.content);
                    article.url = '#article/' + article._id;
                }
                that.articles(response.articles);
            });
        },
        binding: function () {
            system.log('Lifecycle : binding : hello');
            return { cacheViews:false }; //cancels view caching for this module, allowing the triggering of the detached callback
        },
        bindingComplete: function () {
            system.log('Lifecycle : bindingComplete : hello');
        },
        attached: function (view, parent) {
            system.log('Lifecycle : attached : hello');
        },
        compositionComplete: function (view) {
            system.log('Lifecycle : compositionComplete : hello');
        },
        detached: function (view) {
            system.log('Lifecycle : detached : hello');
        }
    };
});
