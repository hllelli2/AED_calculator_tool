import gffpandas.gffpandas as gffpd

annotation = gffpd.read_gff3("gene1_ann.gff")
evidence = gffpd.read_gff3("gene2_ev.gff")

ann_exon_df = annotation.filter_feature_of_type(["exon"])
intervals_ann = ann_exon_df.df[["start", "end"]].values.tolist()

ev_exon_df = evidence.filter_feature_of_type(["exon"])
intervals_ev = ev_exon_df.df[["start", "end"]].values.tolist()

overlap_count = 0
non_overlap_count = 0

for int2 in intervals_ann:
    start2, end2 = int2
    # Loop through every integer value in the range int2 (inclusive)
    for value in range(start2, end2 + 1):
        found_overlap = False
        # Check if the current value falls within any interval in intervals1
        for int1 in intervals_ev:
            start1, end1 = int1
            if start1 <= value <= end1:  # inclusive boundaries
                found_overlap = True
                break
        if found_overlap:
            overlap_count += 1
        else:
            non_overlap_count += 1

print("Number of overlapping values:", overlap_count)
print("Number of non-overlapping values:", non_overlap_count)


