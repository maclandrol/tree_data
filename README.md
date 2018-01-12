# tree_data

### Quest For orthologs 
- https://questfororthologs.org/standards 
- Le site du benchmark est à : http://orthology.benchmarkservice.org/cgi-bin/gateway.pl
- Le papier d’intérêt qui explique les différentes mesures : https://www.nature.com/articles/nmeth.3830 . Tu peux jetter un oeil aux papiers suivants aussi  pour te faire une idée :
  - Relation entre orthologues et fonctions: http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002514
  - Base de donnée liant des protéines de Uniprot à des termes GO : https://academic.oup.com/nar/article/40/D1/D565/2902817 
  - Similarité fonctionnelle de Schlicker: (il se peut que de meilleures mesures existent) https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-7-302
  - Survol ce papier  aussi  si tu as le temps: http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000262 
- Et l’implémentation actuelle du service est disponible à https://github.com/qfo/benchmark-webservice
- Protéome de référence : https://www.ebi.ac.uk/reference_proteomes
Le benchmark se fait sur la release de 2011:  ftp.ebi.ac.uk/pub/databases/reference_proteomes/previous_releases/qfo_release-2011_04/ 
Dans le protéome de référence il y a des familles qui font partie des “gold standards” de Swisstree. L’efficacité des méthodes est même mesurée sur ces familles.  Comme arbre de test, tu peux considérer l’une de ces familles. 

### SwissTree 
https://swisstree.vital-it.ch/species_tree , pour une raison que j’ignore le lien vers les téléchargements ne fonctionne plus. Il est toujours possible de télécharger certains arbres (mais pas les alignements). Tu trouveras dans le répertoire les familles de références que j'avais sur mon laptop

### Ensembl Compara
- Il est possible de télécharger l'entièreté des familles et les arbres corresponds pour la release 73.
ftp.ensembl.org/pub/release-73/emf/ensembl-compara/homologies/ 
- Tu trouveras les séquences protéiques Compara.73.protein.aa.fasta.gz, mais aussi leur alignements Compara.73.protein.aln.emf.gz et les arbres de gènes Compara.73.protein.nh.emf.gz / Compara.73.protein.nhx.emf.gz en format newick que tu peux facilement lire avec ete3 (http://etetoolkit.org/) en python ou ape/phytools en R. 
- Dans l'archive profile_data.zip, il y a également pour chaque famille de gène d'ensembl, l'alignement, l'arbre phyml et les outputs de la correction par profileNJ ( un de nos outils disponible à https://github.com/maclandrol/profileNJ ). 
- Check : https://github.com/Ensembl pour les outils d'ensembl, ce sera util pour construire les familles de gènes plus tard. 

### OrthoBench 
Il s'agit d'un autre service de benchmarking qui comprends des orthogroups manuellement vérifiés. 
Le papier est disponible https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3193375/  et le lien du service est : http://eggnog.embl.de/orthobench/ 


