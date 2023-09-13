import argparse
from SELFRec import SELFRec
from util.conf import ModelConf

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, default='BPR', help='name of models')
    args, _ = parser.parse_known_args()
    
    graph_baselines =  [
        'LightGCN',
        'LightGCN_Weight',
        'LightGCN_NonConcat',
        'LightGCN_Egress',
        'LightGCN_Weight_Egress',
        'LightGCN_NonConcat_Egress',
        'DirectAU',
        'MF',
        'WTGF'
    ]
    
    ssl_graph_models = [
        'SGL',
        'SGL_Egress',
        'SGL_Weight',
        'SGL_Weight_Egress',
        'SGL_NonConcat',
        'SGL_NonConcat_Egress',
        'SGL_AED',
        'SimGCL',
        'SimGCL_Egress',
        'SimGCL_Weight',
        'SimGCL_Weight_Egress',
        'SimGCL_NonConcat',
        'SimGCL_NonConcat_Egress',
        'SEPT',
        'MHCN',
        'BUIR',
        'BUIR_Egress',
        'BUIR_Weight',
        'BUIR_Weight_Egress',
        'BUIR_NonConcat',
        'BUIR_NonConcat_Egress',
        'SelfCF',
        'SSL4Rec',
        'XSimGCL',
        'XSimGCL_Egress',
        'XSimGCL_Weight',
        'XSimGCL_Weight_Egress',
        'XSimGCL_NonConcat',
        'XSimGCL_NonConcat_Egress',
        'NCL',
        'NCL_Egress',
        'NCL_Weight',
        'NCL_Weight_Egress',
        'NCL_NonConcat',
        'NCL_NonConcat_Egress',
        'MixGCF',
        'MixGCF_Egress'
        'MixGCF_Weight',
        'MixGCF_Weight_Egress',
        'MixGCF_NonConcat',
        'MixGCF_NonConcat_Egress',
    ]
    
    sequential_baselines= [
        'SASRec'
    ]
    
    ssl_sequential_models = [
        'CL4SRec',
        'DuoRec',
        'BERT4Rec'
    ]

    print('=' * 80)
    print('   SELFRec: A library for self-supervised recommendation.   ')
    print('=' * 80)
    print('Graph-Based Baseline Models:')
    print('   '.join(graph_baselines))
    print('-' * 100)
    print('Self-Supervised  Graph-Based Models:')
    print('   '.join(ssl_graph_models))
    print('=' * 80)
    print('Sequential Baseline Models:')
    print('   '.join(sequential_baselines))
    print('-' * 100)
    print('Self-Supervised Sequential Models:')
    print('   '.join(ssl_sequential_models))
    print('=' * 80)
    
    # model = input('Please enter the model you want to run:')
    model = args.model
    
    import time
    s = time.time()
    if model in graph_baselines or model in ssl_graph_models or model in sequential_baselines or model in ssl_sequential_models:
        conf = ModelConf('./conf/' + model + '.conf')
    else:
        print('Wrong model name!')
        exit(-1)
    rec = SELFRec(conf)
    rec.execute()
    e = time.time()
    print("Running time: %f s" % (e - s))