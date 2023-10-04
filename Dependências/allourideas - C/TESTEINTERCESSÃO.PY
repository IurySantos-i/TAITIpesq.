import pandas as pd




df = pd.read_csv('https___github.com_allourideas_allourideas.org.csv',engine="python", sep=';')
print(df)
Taiti= df.at[11,'TestI'][1:-1].split(",")
Taiti = [x.strip(' ') for x in Taiti]
print(Taiti)
Changed= df.at[11,'Changed files'][1:-1].split(",")
Changed = [x.strip(' ') for x in Changed]
print(Changed)



def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
lST = ['app/views/choices/show.html.haml', 'config/routes.rb', 'features/admin/flag_as_inappropriate_choice.feature', 'features/results/paginate_all_results.feature', 'features/results/view_individual_idea_page.feature', 'features/results/view_results.feature', 'features/step_definitions/admin_steps.rb', 'features/step_definitions/idea_marketplace_steps.rb', 'features/step_definitions/voting_steps.rb', 'features/support/paths.rb', 'features/voting/cantdecide.feature', 'features/voting/leveling_adjectives.feature', 'features/voting/voting.feature, test/factories/question.rb']
lST2 = ['app/controllers/choices_controller.rb', 'app/models/choice.rb', 'app/models/earl.rb', 'app/models/prompt.rb', 'app/models/question.rb', 'app/views/abingo_dashboard/_experiment_row.html.haml', 'app/views/abingo_dashboard/index.html.haml', 'app/views/choices/show.html.haml', 'app/views/shared/_header_vote.html.haml']
print(intersection(lST,lST2))
