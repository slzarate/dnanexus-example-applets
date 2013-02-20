#!/usr/bin/env python
# tumor_normal_snp_pipeline 0.0.1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# See http://wiki.dnanexus.com/Building-Your-First-DNAnexus-App for
# instructions on how to modify this file.
#
# DNAnexus Python Bindings (dxpy) documentation:
#   http://autodoc.dnanexus.com/bindings/python/current/

import os
import dxpy

@dxpy.entry_point('main')
def main(tumor_left_reads, tumor_right_reads, normal_left_reads, normal_right_reads, reference,
         indexed_reference, dbsnp, known_indels, aln_params="", reads_per_chunk=25000000, indel_realigner_params="", samse_sampe_params="-r '@RG\tID:1\tPL:ILLUMINA\tPU:None\tLB:1\tSM:1'",
         mark_duplicates_params="ASSUME_SORTED=true VALIDATION_STRINGENCY=LENIENT", count_covariates_params="", table_recalibrator_params="", somatic_sniper_params="-F vcf"):

    tumor_alignment_job = applet("bwa_recalibration_pipeline").run({"left_reads": tumor_left_reads, "right_reads": tumor_right_reads, "reference": reference, "indexed_reference": indexed_reference,
                                                                     "reads_per_chunk": reads_per_chunk, "aln_params": aln_params, "samse_sampe_params": samse_sampe_params,
                                                                     "dbsnp": dbsnp, "known_indels": known_indels, "mark_duplicates_params": mark_duplicates_params, "count_covariates_params": count_covariates_params,
                                                                     "table_recalibrator_params": table_recalibrator_params})

    normal_alignment_job = applet("bwa_recalibration_pipeline").run({"left_reads": normal_left_reads, "right_reads": normal_right_reads, "reference": reference, "indexed_reference": indexed_reference,
                                                                     "reads_per_chunk": reads_per_chunk, "aln_params": aln_params, "samse_sampe_params": samse_sampe_params,
                                                                     "dbsnp": dbsnp, "known_indels": known_indels, "mark_duplicates_params": mark_duplicates_params, "count_covariates_params": count_covariates_params,
                                                                     "table_recalibrator_params": table_recalibrator_params})

    somatic_sniper_job = applet("somatic_sniper").run({"tumor_bam": {"job": tumor_alignment_job.get_id(), "field": "recalibrated_bam"}, "normal_bam": {"job": normal_alignment_job.get_id(), "field": "recalibrated_bam"},
                                                        "reference": reference, "params": somatic_sniper_params})

    output = {"tumor_bam": {"job": tumor_alignment_job.get_id(), "field": "recalibrated_bam"}, "normal_bam": {"job": normal_alignment_job.get_id(), "field": "recalibrated_bam"}, "snps": {"job": somatic_sniper_job.get_id(), "field": "snps"}}

    return output

def applet(name):
    return find_in_project(name=name, classname="applet", return_handler=True)

def find_in_project(**kwargs):
    kwargs["project"] = os.environ["DX_PROJECT_CONTEXT_ID"]
    return dxpy.find_one_data_object(**kwargs)

dxpy.run()
