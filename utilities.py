from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, make_scorer, f1_score, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

def prepare_models(clfs_to_test, use_scaler=False, use_grid_search=True, verbose=False):
    gs_dict = {}
    clfs_dict = {
        'DTC': DecisionTreeClassifier(random_state=0),
        'RFC': RandomForestClassifier(random_state=0),
        'KNN': KNeighborsClassifier(),
        'LR': LogisticRegression(random_state=0, multi_class='multinomial', solver='lbfgs')
    }

    param_grids = {
        'DTC': {
            '__class_weight': [None, 'balanced'],
            '__max_depth': [1, 2, 3, 5, 10, 20, None],
            '__criterion': ['gini', 'entropy'],
#             '__min_samples_split': [0.2, 0.3, 0.5],
#             '__min_weight_fraction_leaf': np.linspace(0.05, 0.4, 5)
#             '__class_weight': [None],
#             '__presort': [False],
#             '__max_depth': [3],
#             '__criterion': ['entropy'],
#             '__min_samples_split': [0.2],
#             '__min_weight_fraction_leaf': [0.1]
        },
        'RFC': {
            '__class_weight': [None],
            '__n_estimators': [100],
            '__max_depth': [30],
            '__class_weight': ['balanced']

        },
        'KNN': {
            '__n_neighbors': [10],
            '__weights': ['distance'],
            # '__n_neighbors': range(7, 13),
            # '__weights': ['uniform', 'distance'],
        },
        'LR': {
            "__C": [0.01,0.1,1.0]            
        }
    }
    # scorer = make_scorer(f1_score, average='micro')
    clfs_dict = {your_key: clfs_dict[your_key] for your_key in clfs_to_test}
    for clf_name in clfs_dict:
        if use_scaler:
            pipe_line = Pipeline([('scaler', StandardScaler()), ('', clfs_dict[clf_name])])
        else:
            pipe_line =  Pipeline([('',clfs_dict[clf_name])])

        if use_grid_search:
            gs = GridSearchCV(pipe_line, param_grid=param_grids[clf_name], cv=8, verbose=verbose,
                              iid=True)
        else:
            gs = pipe_line
        gs_dict[clf_name] = gs
    return gs_dict


def model_selection(clfs_to_test, x_train, x_valid, y_train, y_valid):
    gs_dict = prepare_models(clfs_to_test, use_scaler=False, use_grid_search=True, verbose=False)
    for gs_name in gs_dict:
        print("\n==================================================================\n", gs_name, end="\t")
        gs = gs_dict[gs_name].fit(x_train, y_train)
        print("\tAccuracy Train: ", np.round(100 * accuracy_score(y_train, gs.predict(x_train)), 1), "%", sep="",
              end="")
        print("\tAccuracy Valid: ", np.round(100 * accuracy_score(y_valid, gs.predict(x_valid)), 1), "%", sep="")
        print("\tBest params: ")
        for param in gs.best_params_:
            print("\t\t\'", param, "\': ", "[", gs.best_params_[param], "]", sep="")

        print(pd.DataFrame(confusion_matrix(y_valid, gs.predict(x_valid))))
        # columns=['Predicted 0', 'Predicted 1', 'Predicted 2'],
        # index=['Actual 0', 'Actual 1', 'Actual 2']))
        gs_dict[gs_name] = gs
    return [(k, v) for k, v in gs_dict.items()]
