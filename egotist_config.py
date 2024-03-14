"""Configuration settings to be used by egotist"""

## dictionary of cluster definitions across teams
dept_stack = {
    "gamma": {
        "Dev": {
            "dev":[
                {"stack":"aws-aps1-gamma-grvcp","owner":"ashutosh.mittal@amagi.com","description":"cp development arm setup"},
                {"stack":"aws-aps1-gamma-sks02","owner":"ashutosh.mittal@amagi.com","description":"cp tally development setup"},
                {"stack":"aws-aps1-gamma-sks02-ds","owner":"sekhar@amagi.com","description":"tally secret"},
                {"stack":"aws-aps1-iota-test1-ds","owner":"sekhar@amagi.com","description":""},
                {"stack":"aws-aps1-gamma-intcp","owner":"karthik.v@amagi.com","description":"cp development intel setup"},
                {"stack":"aws-aps1-iota-test1","owner":"sekhar@amagi.com","description":""},
                {"stack":"aws-aps1-gamma-common","owner":"ashutosh.mittal@amagi.com","description":"deployment servers"}
            ],
            "mapsor": [ {"stack":"mapsor-compute-mumbai","owner":"veeranjaneyulu.m@amagi.com","description":"mapsor"}],
            "customisation": [{"stack":"aws-aps1-gamma-custo","owner":"vinayagar@amagi.com","description":"cp development setup for customization team"}]
        }
    },
    "alpha": {
        "Dev":{
            "dev":[
                {"stack":"aws-aps1-alpha-mango","owner":"chirag.jain@amagi.com","description":"cplive integration development testing"},
                {"stack":"aws-apse1-alpha-scnd1","owner":"shiva.b@amagi.com","description":"crr development setup"},
                {"stack":"aws-apse1-alpha-tea-sec","owner":"shiva.b@amagi.com","description":"crr development setup"},
                {"stack":"aws-apse1-alpha-tea","owner":"shiva.b@amagi.com","description":"crr development setup"},
                {"stack":"aws-aps1-alpha-tea","owner":"shiva.b@amagi.com","description":"dev qa and longhaul testing"},
                {"stack":"TR07","owner":"shiva.b@amagi.com","description":"Source players for cplive testing"},
                {"stack":"deployment-server","owner":"shiva.b@amagi.com","description:"deployment servers for pulumi deployments"}
            ]
        }
    },
    "beta": {
        "Dev":{
            "dev":[
                {"stack":"aws-use1-dev-beta1","owner":"gavi@amagi.com","description":"cp 3.11 bug validation setup for dazn"},
                {"stack":"Iota-bolt","owner":"gavi@amagi.com","description":"Setup for QA Team"},
                {"stack":"aws-as1-iota-idpb1","owner":"manav.nanwani@amagi.com","description":"Setup for QA Team"},
                {"stack":"aws-use1-beta-qaue2","owner":"arindam@amagi.com","description":"Setup for QA Team"},
                {"stack":"aws-use1-beta-sdet","owner":"pranchal.sihare@amagi.com","description":"Setup for QA Team"},
                {"stack":"aws-use1-beta-set4","owner":"ieg-idp@amagi.com","description":"Setup for QA Team"},
		{"stack":"aws-use1-beta-qa1","owner":"gavi@amagi.com","description":"Setup for v7.5.26 blip version bugs validation"},
		{"stack":"aws-use1-beta-qa2","owner":"gavi@amagi.com","description":"Setup for v7.5.26 blip version bugs validation- setup2"},
		{"stack":"aws-use1-beta-qa3","owner":"gavi@amagi.com","description":"Setup for NBCU cpprod channels bug validation- setup3"},
		{"stack":"aws-use1-beta-qa4","owner":"gavi@amagi.com","description":"Setup for v7.5.21 cpprod channels bug validation- setup4"},
		{"stack":"aws-use1-beta-qa5","owner":"gavi@amagi.com","description":"Setup for v7.5.21 cpprod channels bug validation- setup5"},
		{"stack":"aws-use1-beta-qa6","owner":"gavi@amagi.com","description":"Setup for standalone v7.6.12 release bug validation- setup6"},
		{"stack":"aws-use1-beta-qa7","owner":"gavi@amagi.com","description":"Stand alone setup resources"}
            ]
        }
    },
    "sigma": {
        "Dev":{
            "dev":[{"stack":"aws-aps1-sigma-sig01","owner":"hamza@amagi.com","description":"Player,DD development and longhaul testing"},{"stack":"aws-aps1-sigma-nonk8s","owner":"hamza@amagi.com","description":"Dev non k8s env for player,DD,capsequo,alta"}]
        }
    },
    "theta": {
        "Dev":{
            "dev":[
                {"stack":"aws-aps1-theta-dev","owner":"karthik.v@amagi.com","description":"Amagi Dynamic product development and testing"},
                {"stack":"aws-euc1-dev-theta-ds","owner":"robert.marinic@amagi.com","description":"coreservice amgctl for platform creation and application deployment"},
                {"stack":"aws-euc1-dev-theta","owner":"robert.marinic@amagi.com","description":"coreservice amgctl for platform creation and application deployment"},
                {"stack":"aws-use1-cpdev-teta1","owner":"","description":""}
            ]
        }
    },
    "omega": {
        "Dev":{
            "dev":[{"stack":"aws-aps1-omega-cpdev","owner":"vaibhav@amagi.com","description":"functional testing for new features"},{"stack":"turn-server","owner":"shuvayan.chakraborty@amagi.com","description":"turn server"}]
        }
    },
    "lambda": {
        "Dev":{
            "dev":[
                {"stack":"aws-aps1-lambda-dev2","owner":"karthik.v@amagi.com","description":"longhaul testing"},
                {"stack":"aws-aps1-lambda-cpdev","owner":"karthik.v@amagi.com","description":"functional testing of features"},
                {"stack":"aws-as1-lambda-pcp1","owner":"chandratop.chakraborty@amagi.com","description":"region migration"},
                {"stack":"lambda-janus","owner":"Varun","description":"Janus Server"},
		{"stack":"aws-aps1-lambda-test","owner":"tharadevi.sr@amagi.com","description":"feature testing using standalone resources"},
		{"stack":"deployment-server","owner":"tharadevi.sr@amagi.com","description":"common deployment servers"},
		    
            ]
        }
    },
    "iota": {
        "qa": {
	    "common-env": [
                {"stack":"aws-aps1-iota-qeng","owner":"rohini.b@amagi.com","description":"New IEG-CP managed env for QA"},
		{"stack":"aws-aps1-iota-qeng-ds","owner":"rohini.b@amagi.com","description":"New IEG-CP managed env for QA"}
            ],	
            "GA": [
                {"stack":"aws-as1-iota-gapub","owner":"jasmin@amagi.com","description":"GA Features Testing & Test Automation & PIE/NPIE Testing"},
                {"stack":"aws-as1-iota-pubqa","owner":"gavi@amagi.com","description":"PIE/NPIE Testing"},
		{"stack":"aws-as1-iota-pubq1","owner":"chaduvula.akhil@amagi.com","description":"PIE/NPIE Testing"}
            ],
            "regression": [
                {"stack":"aws-use1-iota-nb325","owner":"c-prapulla.c@amagi.com","description":"Regression Testing & Test Automation"},
                {"stack":"aws-as1-iota-nb325","owner":"c-prapulla.c@amagi.com","description":"Regression MRR Testing"},
                {"stack":"aws-use1-iota-nbc41","owner":"c-prapulla.c@amagi.com","description":"Regression Testing"}
            ],
            "nbcu": [
                {"stack":"aws-use1-iota-dep41","owner":"rohini@amagi.com","description":"NBCU Deployment Testing 4.1"},
                {"stack":"aws-use1-iota-qadep","owner":"rohini@amagi.com","description":"Deployment Testing 3.31"},
                {"stack":"aws-use2-iota-vp321","owner":"rohini@amagi.com","description":"NBCU CPRE 3.23 Testing"},
                {"stack":"aws-use1-iota-cp321","owner":"shashi.raja@amagi.com","description":"NBCU CPRE 3.23 Testing & Test Automation"},
                {"stack":"nbcu-rdp","owner":"goutham.bs@amagi.com","description":"RDP for private setup"},
                {"stack":"nb325-mapsor-compute-env","owner":"rohini@amagi.com","description":"Mapsor for nb325 setup"},
                {"stack":"aws-use1-cp-vod-mapsor-compute-env","owner":"akash.gupta@amagi.com","description":"cp_vod Testing"},
                {"stack":"mapsor-compute-env-depnew1","owner":"rohini@amagi.com","description":"CPRE Testing"},
                {"stack":"aws-as1-iota-vp41","owner":"rohini@amagi.com","description":"Functional & Regression Testing"},
	        {"stack":"aws-use1-nbcu-cp-vod","owner":"nishmitha.p@amagi.com","description":"Stack used for cp-vod QA deployment testing"},
		{"stack":"nbcu-cp-vod","owner":"nishmitha.p@amagi.com","description":"Stack used for cp-vod QA deployment testing"},
		{"stack":"cpvod-deployment","owner":"kavya.m@amagi.com","description":"Stack used for cp-vod QA testing"},
		{"stack":"aws-use1-cpvod-deployment","owner":"kavya.m@amagi.com","description":"Stack used for cp-vod QA testing"},
                {"stack":"aws-use1-iota-dp411","owner":"prem.sagar@amagi.com","description":"Deployment testing for cp_4.1"},
                {"stack":"aws-use1-iota-tally","owner":"nishmitha.p@amagi.com","description":"Coreservice and mtao deployment"},
                {"stack":"aws-use1-iota-mtao","owner":"nishmitha.p@amagi.com","description":"Coreservice and mtao deployment"},
                {"stack":"aws-use1-iota-dp125","owner":"rohini@amagi.com","description":"KASA Testing"},
                {"stack":"aws-use1-iota-eks25","owner":"rohini@amagi.com","description":"cp_3.23 eks Upgrade testing"},
		{"stack":"aws-as1-iota-qa331","owner":"rohini@amagi.com","description":"KASA MRR Setup 3.31"}
            ],
            "crr": [
                {"stack":"aws-aps1-iota-sind3","owner":"chaduvula.akhil@amagi.com","description":"CRR QA Setup"},
                {"stack":"aws-apse1-iota-sind4","owner":"chaduvula.akhil@amagi.com","description":"CRR QA Setup"}
            ],
            "bolt": [
                {"stack":"aws-use1-iota-pblt1","owner":"hema.upadhayay@amagi.com","description":"Bolt Testing"}, 
                {"stack":"iota-pblt1-new-mapsor-compute-env","owner":"goutham.bs@amagi.com","description":"Mapsor for bolt"},
		{"stack":"bolt","owner":"priyanka.palav@amagi.com","description":"Bolt setup Testing"}    
                ],
            "NPIE/PIE": [
                {"stack":"aws-aps1-iota-qa101","owner":"gavi@amagi.com","description":"LTS testing"}, 
                {"stack":"aws-aps1-iota-qapvm","owner":"gavi@amagi.com","description":"CRR Grafana"}
                ],    
            "common": [
                {"stack":"qa-common","owner":"goutham.bs@amagi.com","description":"standalone ec2 instances for live input source"},
                {"stack":"TR07","owner":"goutham.bs@amagi.com","description":"standalone ec2 instances for live input source of JPEG protocol"}
                ],
        },
        "others": {"product": [{"stack":"aws-use1-iota-ipro7","owner":"karthik.v@amagi.com","description":"Product team cloudport stack"}]},
        "dev": {
            "customisation": [
		    {"stack":"aws-aps1-iota-custo","owner":"sekhar@amagi.com","description":"migration from gamma to iota"},
		    {"stack":"customizaion-team-gamma-resources-migration","owner":"md.ansari@amagi.com","description":"migration of standalone blips from gamma to iota for customization team"},
		    {"stack":"customization-standalone-cplive-setups","owner":"aishwarya@amagi.com","description":""},
		    {"stack":"player_1_cust","owner":"shraddhakhot@amagi.com","description":"QA playout testing"},
		    {"stack":"player_2_cust","owner":"shraddhakhot@amagi.com","description":"QA playout testing"},
		     
	    ],
            "github-runner": [{"stack":"ieg-github-runner","owner":"aman.favas@amagi.com","description":"self hosted github runner for mimas and TR07_muxer repos"},
			      {"stack":"aws-aps1-iota-github-arc","owner":"veeranjaneyulu.m@amagi.com","description":"self hosted github runner on kubernetes cluster"}
			     ],
        },
	"amagi-studio": { "studio":[{"stack":"studio","owner":"kushagra@amagi.com","description":"New product amagi studio testing"}]},
        "ieg-cp": {
            "personal": [
                {"stack":"teleport-iota","owner":"soumya.ranjan@amagi.com","description":"teleport access"},
                {"stack":"jenkins","owner":"ieg-platform+common@amagi.com","description":"Dev jenkins"},
                {"stack":"roshan","owner":"roshan@amagi.com","description":"ec2 instance used for dev like building docker images and debugging dev environments of coreservice"},
                {"stack":"ssm-instance-ecr-copy","owner":"soumya.ranjan@amagi.com","description":"copy ecr image to gcr,rds daily stop scripts"},
                {"stack":"aws-aps1-iota-aktst","owner":"chaduvula.akhil@amagi.com","description":"testing platform deployment scripts"},
                {"stack":"aws-aps1-iota-sk101","owner":"sushant.kumar@amagi.com","description":"Test stack-no longer required"},
                {"stack":"aws-use1-iota-testkv","owner":"karthik.v@amagi.com","description":"Single EC2 instance created for hosting demo app"},
                {"stack":"aws-aps1-iota-mrg71","owner":"sushant.kumar@amagi.com","description":"Infra used for Amagination 2023"},
		{"stack":"pypi","owner":"karthik.k@amagi.com","description":"pypi server"},
		{"stack":"aws-aps1-ing-bench","owner":"pranchal.sihare@amagi.com","description":"Benchmarking on ingress controllers"},
		{"stack":"sre-common","owner":"balamurugan.samiyappan@amagi.com","description":"sre automation and testing"},
		{"stack":"aws-aps1-iota-mns3","owner":"manav.nanwani@amagi.com","description":"Cluster to test new s3 ingest workflow"},
		{"stack":"aws-aps1-iota-mns3-ds","owner":"manav.nanwani@amagi.com","description":"Cluster to test new s3 ingest workflow"},
            ],
            "cpprod": [{"stack":"picasso-dev","owner":"aman.favas@amagi.com","description":" for picasso code changes"}],
            "mapsor": [
                {"stack":"mapsor-compute-mumbai-compute-env","owner":"ieg-platform+mapsor@amagi.com","description":"used by cp envs in mumbai region"},
                {"stack":"use1-mapsor-iota-common-mapsor-compute-env","owner":"ieg-platform","description":"used by cp envs in N.virginia region"},
            ],
            "ieg-coreservices": [
                {"stack":"controlplane-non-prod","owner":"","description":"Dev cluster for Auth Controlplane and FGA"},
                {"stack":"controlplane-prod","owner":"roshan@amagi.com","description":"rds snapshots of old iota/prod setup of old controlplane prod"},
                {"stack":"aws-aps1-roshan-datas","owner":"karan.singh@amagi.com","description":"created for testing by coreservice team"},
                {"stack":"coreservice","owner":"roshan@amagi.com","description":"Infra used by Coreservice and amgctl"},
		{"stack":"aws-aps1-iota-foxtl","owner":"roshan@amagi.com","description":"Amgctl integration - application components"},
            ],
            "pcp": [{"stack":"aws-aps1-nprod-pcp","owner":"pranchal.sihare@amagi.com","description":"Non Prod MTAO Cluster"}, {"stack":"aws-aps1-nprod-pcpds","owner":"pranchal.sihare@amagi.com","description":"DataStack for non prod pcp cluster"}, {"stack":"aws-aps1-sks1-urv01","owner":"sekhar@amagi.com","description":"AMGCTL MTAO Test"}],
            "platform-devqa": [ 
		    {"stack":"aws-use1-iota-csvna-ds","owner":"sushant.kumar@amagi.com","description":"c7a instance type family data stack"},
		    {"stack":"iota-csvna","owner":"sushant.kumar@amagi.com","description":"c7a instance type family; iam role stack"},
		    {"stack":"aws-as1-upg-nbc28","owner":"pranchal.sihare@amagi.com","description":"Stack to test EKS 1.25 upgrade for NBCU"},
	    ],
            "observability": [
                {"stack":"dr-box-handover","owner":"jyotir.adityagiri@amagi.com","description":"Used for infra components validation in DR box"},
		{"stack":"aws-as1-iota-jacp","owner":"jyotir.adityagiri@amagi.com","description":"Dev n Testing env for graceful node termination and image caching"},
                {"stack":"aws-aps1-iota-akpcp","owner":"ayush.kumar@amagi.com","description":"Used as testing environment for observability"},
                {"stack":"aws-aps1-iota-akds1","owner":"ayush.kumar@amagi.com","description":"Used as testing environment for observability"}, 
		{"stack":"aws-aps1-iota-cauto","owner":"ronak.kogta@amagi.com","description":"Used as testing environment for karpenter"},
		{"stack":"aws-aps1-iota-cpkar","owner":"ronak.kogta@amagi.com","description":"Used as testing environment for karpenter"},
		{"stack":"aws-as1-iota-pssg","owner":"ronak.kogta@amagi.com","description":"Stack used for testing prometheus discovery mechanism changes for player metrics | Used as testing environment for karpenter"},
		{"stack":"aws-as1-iota-proup","owner":"pranchal.sihare@amagi.com","description":"Stack used for testing changes in platform resources"}
            ],            
            "amgctl-clusters": [{"stack":"aws-aps1-iota-gmapb","owner":"sekhar@amagi.com","description":"Devqa & Dev gamma"},{"stack":"aws-aps1-iota-gmapb-ds","owner":"sekhar@amagi.com","description":"Devqa & Dev gamma"}],
            "prod_upgrade": [
                {"stack":"aws-as1-iota-vcur","owner":"balamurugan.samiyappan@amagi.com","description":"staging setup for CP305"},
                {"stack":"aws-aps1-iota-vnext","owner":"balamurugan.samiyappan@amagi.com","description":"feature  for amgctl"},
                {"stack":"aws-use1-iota-csvna","owner":"sushant.kumar@amagi.com","description":"Testing for adding SG to NLB"},
		{"stack":"aws-aps1-iota-clone","owner":"chandratop.chakraborty@amagi.com","description":"Cluster for cloning a production customer to test cp upgrades"},
            ],
            "platform-dashboard": [{"stack":"platform-dashboard","owner":"manav.nanwani@amagi.com","description":"Used to host the platform dashboards"}],
            "skynet": [{"stack":"skynet","owner":"chaduvula.akhil@amagi.com","description":"skynet deployment in IOTA"}],
            "imagine-dynamic": [{"stack":"imagine-deployment","owner":"aviators@imaginecommunications.com","description":"imagine canadian team development/testing"}, {"stack":"aws-use1-iota-intgn","owner":"manav.nanwani@amagi.com","description":"used by imagine/dynamic team"}, {"stack":"aws-use1-iota-intgn-ds","owner":"manav.nanwani@amagi.com","description":"used by imagine/dynamic team"}, {"stack":"imagine","owner":"manav.nanwani@amagi.com","description":"deployment server for imagine"}],
            "amgctl":[{"stack":"iota_aps1_kk_amgctl","owner":"karthik.k@amagi.com","description":"created vpc for testing mtao"}],
	    "tellyopro":[
		    {"stack":"tellyopro","owner":"jerzy.wisniewski@amagi.com","description":"tellyo"}, 
		    {"stack":"aws-aps1-tellyo-pro","owner":"manav.nanwani@amagi.com","description":"tellyopro integration testing"}
	    ]
        },
        "ieg-an": {
            "an-cpprod2": [
                {"stack":"aws-use1-iota-stag1","owner":"ajay.kamath@amagi.com","description":"Used by amaginow staging environment"},
                {"stack":"aws-use1-iota-atest","owner":"ajay.kamath@amagi.com","description":"Used by amaginow test environment"},
                {"stack":"aws-use1-iota-adevn","owner":"ajay.kamath@amagi.com","description":"Used by amaginow dev environment"},
                {"stack":"ancp-dev-db-stack","owner":"ka.venkatasubramaniyan@amagi.com","description":""},
                {"stack":"aws-use1-iota-amaginow","owner":"","description":""},
            ],
            "cp-vod": [
                    {"stack":"aws-use1-cp-vod-dev","owner":"harisanker.a@amagi.com","description":"Stack used by cp-vod devs to deploy and test new features for NBCU"},
                    {"stack":"cp-vod-dev","owner":"harisanker.a@amagi.com","description":"Stack used by cp-vod devs to deploy and test new features for NBCU"},
            ]
        },
        "ieg-observability" : {
	    "karpenter": [ 
            	{"stack": "aws-aps1-iota-iacm1", "owner": "chaitanya.k@amagi.com", "description": "for the POC purpose of karpenter, kyverno and vcluster"},
            	{"stack": "aws-aps1-iota-karp1", "owner": "chaitanya.k@amagi.com", "description": "for the POC purpose of karpenter, kyverno and vcluster"}
	    ]
	},
	"cp-dev": {
	   "pano": [
		{"stack":"aws-use1-iota-pano1","owner":"ravtr@amagi.com","description":"setup for pre QA integration testing"},
		{"stack":"aws-usw2-iota-pano2","owner":"ravtr@amagi.com","description":"setup for pre QA integration testing"}
	   ],
	   "dazn-load-test": [ 
		{"stack":"aws-aps1-iota-dazn","owner":"md.ansari@amagi.com","description":"Dazn like setup for load testing,used by-shiva.b@amagi.com"}
	   ]
	},
	"iota-common": {
	   "common-nat":[
                {"stack":"aws-use1-common","owner":"pranchal.sihare@amagi.com","description":"Common resources in us-east-1 used by CP envs"}, 
                {"stack":"aws-aps1-common","owner":"pawan.sikawat@amagi.com","description":"mapsor and serverless bucket and common NAT"},  
                {"stack":"aws-apse1-common","owner":"chaduvula.akhil@amagi.com","description":"common rds,elasticache,vpc resources and NAT"}	   
	   ],
	  "common-infra":[
                {"stack":"aws-aps1-iota-cmrds","owner":"karthik.v@amagi.com","description":"Common RDS stack is being used by all the cloudport dev teams in us-east-1"},
                {"stack":"aws-usw2-iota-cmrds","owner":"chandratop.chakraborty@amagi.com","description":"Common RDS stack is being used by all the cloudport dev teams in us-west-2"},
                {"stack":"aws-use1-iota-cmrds","owner":"karthik.v@amagi.com","description":"Common RDS stack is being used by all the cloudport dev teams in ap-south-1"},
                {"stack":"aws-aps1-common","owner":"ieg-platform+common@amagi.com","description":"Common resources used by CP envs"},
		{"stack":"iota-common-mapsor-compute-env","owner":"ieg-platform+mapsor@amagi.com","description":"Common resources used by CP envs"},
                {"stack":"aws-usw2-common","owner":"chandratop.chakraborty@amagi.com","description":"Common resources in us-west-2 used by CP envs"},
                {"stack":"aws-use2-common","owner":"pranchal.sihare@amagi.com","description":"Common resources in us-east-2 used by CP envs"},
                {"stack":"aws-use1-iota-controlplane-non-prod","owner":"karthik.v@amagi.com","description":"Non prod PCP which host argo and observability stack"},
		{"stack":"aws-aps1-iota-red7","owner":"soumya.ranjan@amagi.com","description":"This Common Elasticache Redis 7 cluster"},
                {"stack":"deployment-server","owner":"veeranjaneyulu.m@amagi.com","description":"common deployment server for private setups"},
		{"stack":"chartmuseum-iota-test","owner":"md.ansari@amagi.com","description":"chartmuseum hosted on ec2"},
		{"stack":"iota-mumbai-common-env","owner":"ieg-platform+common@amagi.com","description":"IEG-CP Managed common infrastructure"},
                {"stack":"vpn_creation","owner":"md.ansari@amagi.com","description":"pritunl vpn server"},
	  ]
	}
    },
}

