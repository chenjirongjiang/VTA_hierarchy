## Cellranger usable naming convention requires renaming

for file in *_2.fastq.gz; do
    mv "$file" "$(basename "$file" _2.fastq.gz).fastq.gz"
done


for file in *_R1.fastq.gz; do
    mv "$file" "$(basename "$file" _R1.fastq.gz)_S1_L001_R1_001.fastq.gz"
done

for file in *_R2.fastq.gz; do
    mv "$file" "$(basename "$file" _R2.fastq.gz)_S1_L001_R2_001.fastq.gz"
done

for file in *_I1.fastq.gz; do
    mv "$file" "$(basename "$file" _I1.fastq.gz)_S1_L001_I1_001.fastq.gz"
done

## rename files with prefix
c=0
for file in bamtofastq_S1_L001_R1_00*.fastq.gz; do
    newname=SN_MD5828b_2_${c}"$(echo "$file" | cut -c11-)"
    mv "$file" "$(basename "$newname" _001.fastq.gz)_001.fastq.gz"
    let c++
done

for file in processed_altena_g0*; do
    newname=processed_altena_base_"$(echo "$file" | cut -c18-)"
    mv "$file" "$newname"
done
######################################################################

##removing big files

for file in * ;
do rm ${file}/outs/possorted_genome_bam.bam ;
done

for file in * ;
do rm ${file}/outs/*feature_bc_matrix.h5 ;
done

for file in * ;
do rm -r ${file}/SC_RNA_COUNTER_CS;
done

for file in * ;
do rm ${file}/*.mri.tgz;
done

for file in * ;
do rm -r ${file}/Solo.out/Gene ;
done

for file in * ;
do rm ${file}/Aligned.out.sam ;
done
######################################################################

##copy all web_summaries in separate folder for extraction

for file in * ;
do cp ${file}/outs/web_summary.html ./websums/${file}.html;
done

for file in * ;
do cp ${file}/outs/metrics_summary.csv   ./websums/${file}.csv;
done

