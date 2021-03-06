import sys

from gprofiler import GProfiler
gp = GProfiler("MyTool/0.1")


inputfile=sys.argv[1]


output_all=inputfile+'.data.enriched.txt'
output_report=inputfile+'.report.enriched.txt'


bnumber=0

with open(inputfile,"r") as data, open(output_all,"w") as output_all_f, open(output_report,"w") as output_report_f:
    for i,line in enumerate(data):
        if i%3==1:
            line=line.strip().split(' ')
            if len(line)>1:
                results=gp.gprofile(line, organism='hsapiens', all_results=False, correction_method=GProfiler.THR_FDR, max_p_value=0.01)
                j=0
                bnumber+=1
                for j,l in enumerate(results):
                    output_all_f.write("Bicluster%d\t" %(bnumber))
                    for item in l:
                        output_all_f.write("%s\t" %(item))
                    output_all_f.write("\n")
                        
                output_report_f.write("Bicluster%s\t%d\n" %(bnumber,j))
                


#results=gp.gprofile(query, organism='hsapiens', all_results=False, ordered=False, region_query=False, exclude_iea=False, underrep=False, evcodes=False, hier_sorting=False, hier_filtering=None, max_p_value=0.00001, min_set_size=None, max_set_size=None, min_isect_size=None, max_isect_size=None, correction_method=None, domain_size=None, numeric_ns=None, custom_bg=None, src_filter=None)
