define(['durandal/app', 'durandal/system', 'knockout', 'plugins/http', 'marked', 'config'], function (app, system, ko, http, marked, config) {
    return {
        title: ko.observable(),
        content: ko.observable(),
        activate: function(id) {
            system.log('Lifecycle : activate : hello');
            var that = this;

            qs = {'id': id};
            return http.get(config.base_url + "article/detail", qs).then(function(response) {
                that.title(response.title);
                that.content(marked(response.content));
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
