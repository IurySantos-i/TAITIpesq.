import os
import subprocess


lista = ['https://github.com/BTHUNTERCN/bsmi.git','https://github.com/EFForg/action-center-platform.git','https://github.com/allourideas/allourideas.org.git','https://github.com/alphagov/e-petitions.git','https://github.com/otwcode/otwarchive.git','https://github.com/sachac/quantified.git','https://github.com/sharetribe/sharetribe.git','https://github.com/sanger/sequencescape.git','https://github.com/rapidftr/RapidFTR.git','https://github.com/opf/openproject.git','https://github.com/opengovernment/opengovernment.git','https://github.com/oneclickorgs/one-click-orgs.git','https://github.com/ministryofjustice/Claim-for-Crown-Court-Defence.git','https://github.com/jekyll/jekyll.git','https://github.com/gleneivey/wontomedia.git','https://github.com/gitlabhq/gitlabhq.git','https://github.com/diaspora/diaspora.git','https://github.com/lisyk/enroll-copy-my.git','https://github.com/alphagov/whitehall.git']

def clone_repos(repo_list, folder_path):
    for repo_url in repo_list:
        os.chdir(folder_path)
        subprocess.run(['git', 'clone', repo_url])

print(len(lista))
clone_repos(lista,r'/home/iury/Taiti_Pesquisa/Repositórios_necessários')