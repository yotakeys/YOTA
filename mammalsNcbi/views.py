from django.shortcuts import render
from gradio_client import Client
from .models import Mammals

# Create your views here.


def index(request):
    data = []
    description = ""
    file_type = {
        "Genome Sequences": "GENOME_FASTA",
        "Annotation features (GFF)": "GENOME_GFF",
        "Sequence and annotation (GBFF)": "GENOME_GBFF",
        "Transcripts (FASTA)": "RNA_FASTA",
        "Genomic coding sequences (FASTA)": "CDS_FASTA",
        "Protein (FASTA)": "PROT_FASTA",
        "Sequence report (JSONL)": "SEQUENCE_REPORT"
    }

    if request.method == "POST":
        description = request.POST.get('description')
        amount = 5

        client = Client(
            "https://yotakey-mammals-search.hf.space/--replicas/66lqq/")
        result = client.predict(
            description,
            amount,
            api_name="/predict"
        )

        data_mammals = result.split(",\n")

        data = Mammals.objects.filter(
            organism_name__in=data_mammals)

        filetype_used = "," + file_type['Genome Sequences'] \
                            + "," + file_type['Sequence report (JSONL)']
        for idx in range(len(data)):
            temp = data[idx].url_download
            index_filtype = temp.find('DEFAULT')
            temp = temp[:index_filtype + len(
                'DEFAULT')] + filetype_used + temp[index_filtype + len('DEFAULT'):]
            data[idx].url_download = temp

    return render(request, "mammalsNcbi/index.html", context={"datas": data, "description": description, "filetype": file_type})
