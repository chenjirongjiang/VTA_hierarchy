##Subset only the necessary Wang download links from the provided script [tightly-coupled/independent]
#(still need to request script before downloading, see https://explore.data.humancellatlas.org/projects/16cd6791-2adb-4d0f-8222-0184dada6456/export-to-terra)
#Used on personal laptop for convenience
script ="""
--create-dirs

--compressed

--location

--globoff

--fail

--fail-early

--continue-at -

--retry 2

--retry-delay 10

--write-out "Downloading to: %{filename_effective}\n\n"

url="https://service.azul.data.humancellatlas.org/repository/files/2987e654-ef7f-41fe-8afb-8b2558642a5c?catalog=dcp28&version=2022-04-07T19%3A26%3A56.716000Z"
output="5d12fe38-12a4-4f00-af18-b902d081624b/SRR16105772_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f425f261-3514-47d1-ac1d-44010a52ca1c?catalog=dcp28&version=2022-04-07T19%3A26%3A55.951000Z"
output="00375e15-335c-4fe8-8ac1-dd456ef205bc/SRR16105753_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/baababe9-f6a6-4914-a384-f62c7f91e7bd?catalog=dcp28&version=2022-04-07T19%3A27%3A45.021000Z"
output="55afffb6-c0a9-451f-9a72-21dc328340ae/SRR16105974_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9ce6e45c-1840-4359-9db4-0a3153115136?catalog=dcp28&version=2022-04-07T19%3A26%3A56.812000Z"
output="30100aa6-2029-4446-b588-2b3dff90fcec/SRR16105775_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08b1b521-221a-4f06-8d6a-99d7bb587c15?catalog=dcp28&version=2022-04-07T19%3A27%3A42.465000Z"
output="87b24f06-ecbe-4233-a1c8-ffc65f6cac25/SRR16105952_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/25110f06-8aa8-456a-bd8d-469358b3c9ac?catalog=dcp28&version=2022-04-07T19%3A28%3A05.153000Z"
output="220d1735-72e0-4f4d-9eac-3afaaa537e9c/SRR16106047_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3fb8df48-4318-472a-847e-e7374f43561b?catalog=dcp28&version=2022-04-07T19%3A27%3A17.534000Z"
output="fad17bc2-c861-4f55-aa68-32f9410d9c99/SRR16105853_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b28f1637-1e00-4c80-8787-4db8e6958878?catalog=dcp28&version=2022-04-07T19%3A28%3A00.656000Z"
output="5e12184a-b091-47a1-9db9-d9174f25dce8/SRR16106037_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a3eb543a-77dd-4740-a74a-94049731f648?catalog=dcp28&version=2022-04-07T19%3A26%3A59.073000Z"
output="beda1d88-0684-4e64-92c9-3b06f44a5e73/SRR16105817_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1bfd8f7c-c55a-4293-97cc-616606d1c74d?catalog=dcp28&version=2022-04-07T19%3A26%3A55.994000Z"
output="2ef00c65-9420-4e92-b23f-9194542914e2/SRR16105754_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cea58205-7506-4358-a322-2491e964fb10?catalog=dcp28&version=2022-04-07T19%3A28%3A08.642000Z"
output="acc0fc8c-a1d8-48c5-a6a1-f5cc80ef5e5e/SRR16106063_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3736d47a-17b3-43cc-9b39-b4d2e5853651?catalog=dcp28&version=2022-04-07T19%3A27%3A15.896000Z"
output="76722270-1b19-4a3d-a588-6747d894cab0/SRR16105841_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/70a91ef8-485b-4c77-8b87-c69dcde824e7?catalog=dcp28&version=2022-04-07T19%3A28%3A10.923000Z"
output="27dc5396-721a-4d2a-8115-09d986f6f605/SRR16106089_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4d97e6f1-25bd-4145-b6d2-a6df55ce3f26?catalog=dcp28&version=2022-04-07T19%3A27%3A29.773000Z"
output="5320df1a-9714-439c-85ea-f23d57ba9c5a/SRR16105901_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b698d903-f51f-4e1f-bdf1-83aadd69068b?catalog=dcp28&version=2022-04-07T19%3A27%3A28.570000Z"
output="f386a906-d9cd-43cb-9020-b134a1bc466a/SRR16105891_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/93745fc8-63f3-4bc5-85e2-2954e023917b?catalog=dcp28&version=2022-04-07T19%3A26%3A58.935000Z"
output="ada83954-9c04-42b3-9bb9-9c0b23070fd6/SRR16105815_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/92ea62a9-c1e6-4093-947a-07fa96778a76?catalog=dcp28&version=2022-04-07T19%3A27%3A32.789000Z"
output="b42b17c1-f6c8-4ec5-a4de-0373439e383f/SRR16105927_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/91df9090-7b0f-4a14-a1e0-0dab25f52b70?catalog=dcp28&version=2022-04-07T19%3A26%3A58.704000Z"
output="9b8aca24-d1fe-4c91-b144-98225db0ac0b/SRR16105810_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ba0c794e-6d22-4a6b-91a6-f0955a3d7f71?catalog=dcp28&version=2022-04-07T19%3A27%3A28.244000Z"
output="f92ab2be-b16d-49d5-9dd6-64a53d44a5f8/SRR16105890_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c3fbcc21-dc38-4fd8-8255-9ba6760bea63?catalog=dcp28&version=2022-04-07T19%3A26%3A56.413000Z"
output="9205f192-10b9-4044-be8b-ed22fac9c1dd/SRR16105764_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d27a326c-7d88-49ce-b44f-872d90fd0d74?catalog=dcp28&version=2022-04-07T19%3A27%3A26.274000Z"
output="e72d2857-7b4b-46aa-88c8-f4f5c63e7eb8/SRR16105884_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cb334abb-917b-47f6-938a-658bdd49afc1?catalog=dcp28&version=2022-04-07T19%3A27%3A18.902000Z"
output="d710d243-2db1-443d-b9d5-b8079b3df6bc/SRR16105864_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b3e657ab-c0c7-41c5-a33f-bfd6a164c64e?catalog=dcp28&version=2022-04-07T19%3A27%3A42.525000Z"
output="45ebc9fb-89e0-4bfa-9a27-56c915f6e58b/SRR16105953_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a4e9f80f-a92b-4c1f-a4c1-332e57e87f41?catalog=dcp28&version=2022-04-07T19%3A27%3A17.922000Z"
output="f9f906cb-3cf3-442d-b264-17b53181fee3/SRR16105856_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8a198302-0ba9-4717-9362-0053ba124774?catalog=dcp28&version=2022-04-07T19%3A26%3A56.666000Z"
output="57e79970-7e14-43b7-8501-905f66922f9b/SRR16105771_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/07381c06-1019-416e-b6cc-2a1270586619?catalog=dcp28&version=2022-04-07T19%3A27%3A44.101000Z"
output="953638a3-828c-4db4-a9b2-85149907861f/SRR16105965_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4b3fa209-3304-45bb-bf53-1e6a98775335?catalog=dcp28&version=2022-04-07T19%3A28%3A09.622000Z"
output="d56edd59-ff53-43c3-bc73-97d1b9fce3d2/SRR16106077_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/205fe028-6ca7-4770-b69f-d99eaabfd7fa?catalog=dcp28&version=2022-04-07T19%3A28%3A12.142000Z"
output="12d2463a-6951-430c-a01f-299db0e16b4b/SRR16106104_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6b5ca85b-4b65-4a25-9b29-a00f2278b49c?catalog=dcp28&version=2022-04-07T19%3A26%3A56.752000Z"
output="e7f33f30-581f-4a1d-be0c-1520c6ec60f2/SRR16105773_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/195f25f7-9049-4e92-8036-86987b56063c?catalog=dcp28&version=2022-04-07T19%3A26%3A56.020000Z"
output="2ef00c65-9420-4e92-b23f-9194542914e2/SRR16105754_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e82ab3e0-e51f-4fa6-8608-d9f9c28b5cb4?catalog=dcp28&version=2022-04-07T19%3A26%3A56.197000Z"
output="0dab1345-3f9c-45c6-a429-671708f38f52/SRR16105759_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1e48877d-2fd1-46a0-82bd-35f57aeca75c?catalog=dcp28&version=2022-04-07T19%3A27%3A57.430000Z"
output="b668566d-5a0d-4839-a3f7-ba746f40ebfe/SRR16106022_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/825e52d7-8d4d-47c0-83e4-c86eff062a35?catalog=dcp28&version=2022-04-07T19%3A27%3A48.692000Z"
output="0443a18a-5a33-4c34-aa6e-3d6fb4c16a05/SRR16105986_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c8892df3-17b4-4409-9227-5126047e1425?catalog=dcp28&version=2022-04-07T19%3A27%3A56.314000Z"
output="40c1e501-6c42-4d72-9326-e698be1241b3/SRR16106011_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7c9d221d-bf0d-45eb-8d8e-991f78ad0058?catalog=dcp28&version=2022-04-07T19%3A27%3A32.379000Z"
output="536b9433-54d3-4fb5-a9cc-f408eb3f9ba9/SRR16105922_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/292e92b6-3a39-43cb-b168-2eddc6de8e9c?catalog=dcp28&version=2022-04-07T19%3A27%3A49.169000Z"
output="0c3336b3-d21e-459c-a1d8-cb792a141631/SRR16105989_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9649b73d-bd16-4eee-bfc7-38af78dc20e5?catalog=dcp28&version=2022-04-07T19%3A27%3A21.405000Z"
output="2bee19a1-6841-4871-9c36-73f1f29349f9/SRR16105880_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a1fc9f4b-a6a4-4c4b-aba4-c65253a150ae?catalog=dcp28&version=2022-04-07T19%3A28%3A12.473000Z"
output="944244ed-be4d-4d23-9686-5fd9dc627ef2/SRR16106111_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9b98298f-ceca-4f3b-a4b0-84053ff1c039?catalog=dcp28&version=2022-04-07T19%3A27%3A00.204000Z"
output="2629e260-5903-478b-a39e-59708cf2052f/SRR16105827_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a67eff60-3d55-4dfb-ae77-c82c8de40277?catalog=dcp28&version=2022-04-07T19%3A27%3A31.836000Z"
output="df64c85a-8709-4400-b9e2-b43a86e206cc/SRR16105917_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a0998119-780d-4ac4-bef1-4152f332cc34?catalog=dcp28&version=2022-04-07T19%3A27%3A48.507000Z"
output="00ab3054-0713-4559-a30a-52622d79bee4/SRR16105985_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fea19eff-bba7-40bb-ab6e-be233c5d35e5?catalog=dcp28&version=2022-04-07T19%3A27%3A32.242000Z"
output="16ecac57-9888-4133-8853-a2daf5aaf528/SRR16105921_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c38a1aab-8b26-430f-8961-60f1ec7fb05b?catalog=dcp28&version=2022-04-07T19%3A27%3A17.630000Z"
output="ac86fd53-27a1-415f-9aa4-1889967604cc/SRR16105854_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/51e1756f-e3b8-42fc-86c9-00df09870ee3?catalog=dcp28&version=2022-04-07T19%3A26%3A57.046000Z"
output="bacaa9c2-8b2a-45a6-9d21-3554b24b3e95/SRR16105777_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2e28ee89-c843-475a-ba68-d24175a3b5d7?catalog=dcp28&version=2022-04-07T19%3A27%3A32.163000Z"
output="8de660b1-fa9e-48da-9d7d-ce171d684923/SRR16105920_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d285a058-1146-47ab-949c-f956b6c10889?catalog=dcp28&version=2022-04-07T19%3A27%3A57.478000Z"
output="b668566d-5a0d-4839-a3f7-ba746f40ebfe/SRR16106022_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1a3e8366-2024-49d0-8cd5-599000cd3490?catalog=dcp28&version=2022-04-07T19%3A27%3A16.417000Z"
output="0d27c127-1fea-4f7b-b54e-4a7a06d8b1cc/SRR16105844_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a98eba22-d73c-4a6d-87d2-e751b479994f?catalog=dcp28&version=2022-04-07T19%3A28%3A08.997000Z"
output="66ceee2f-7c84-458d-b713-bf74a8a93de7/SRR16106070_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4a4c5ccf-a697-454c-a72d-cbd09957361c?catalog=dcp28&version=2022-04-07T19%3A27%3A45.977000Z"
output="832587f4-4111-45b8-b134-5e66f5ee2da5/SRR16105981_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d7bc595a-08c2-496f-9b36-04b292b944c9?catalog=dcp28&version=2022-04-07T19%3A28%3A01.897000Z"
output="3fa51f19-f8ff-46e7-8843-adc53f852b11/SRR16106044_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/da2b37e2-b6a5-4b70-8619-0573a7462c41?catalog=dcp28&version=2022-04-07T19%3A28%3A10.217000Z"
output="8ad0eecd-61c4-4eb3-8201-6d72def553d6/SRR16106086_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/87d46aa1-2764-4ed2-8a49-982fdf98c186?catalog=dcp28&version=2022-04-07T19%3A27%3A42.990000Z"
output="3d2aebd8-a4e0-44fb-8037-b6a1a02fed9a/SRR16105958_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e5bfa1cf-e144-42c7-ae62-f5329ddbda54?catalog=dcp28&version=2022-04-07T19%3A27%3A16.762000Z"
output="34898ed8-5e60-432c-b934-021842b4cfd8/SRR16105848_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c03393e-39a8-435d-b094-74b6723a6355?catalog=dcp28&version=2022-04-07T19%3A27%3A26.839000Z"
output="e72d2857-7b4b-46aa-88c8-f4f5c63e7eb8/SRR16105884_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/78b2a0c5-6d32-4367-9a09-f6b19d311731?catalog=dcp28&version=2022-04-07T19%3A27%3A48.990000Z"
output="d1ad8f6f-5d92-486f-85bf-e8cdba503351/SRR16105988_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0571492f-a9c3-4bc3-a64f-d9e2c661e404?catalog=dcp28&version=2022-04-07T19%3A27%3A54.989000Z"
output="724c2f24-6739-40b4-be89-3c69c7ede75a/SRR16106002_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7061fe15-dffd-4aee-bce8-66c1dbc8bd67?catalog=dcp28&version=2022-04-07T19%3A27%3A17.518000Z"
output="fad17bc2-c861-4f55-aa68-32f9410d9c99/SRR16105853_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c939ab56-9a0f-4ed6-b8d1-8269deb01bba?catalog=dcp28&version=2022-04-07T19%3A26%3A56.976000Z"
output="bacaa9c2-8b2a-45a6-9d21-3554b24b3e95/SRR16105777_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7c6a736e-e1b5-4f42-92fe-21a31483db8c?catalog=dcp28&version=2022-04-07T19%3A27%3A32.688000Z"
output="172012f0-0f31-4241-ad33-272a0efc4a75/SRR16105925_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/12656c40-51d1-4bb3-a859-ca57392bef4a?catalog=dcp28&version=2022-04-07T19%3A27%3A43.940000Z"
output="560607c8-3d51-4dd2-866f-4c09fb872727/SRR16105963_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1f8f4e45-604b-4be1-9524-c53bbfaa9a81?catalog=dcp28&version=2022-04-07T19%3A27%3A18.237000Z"
output="74d703e4-3167-4670-8f16-86007d947783/SRR16105859_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8f2756e9-0906-4053-ab30-6571b7ae4209?catalog=dcp28&version=2022-04-07T19%3A28%3A05.266000Z"
output="975d507d-3c7e-41f6-905e-93e9460d3108/SRR16106048_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ea78ce59-abaa-446c-ae24-c5a215cf3214?catalog=dcp28&version=2022-04-07T19%3A28%3A10.485000Z"
output="723d3641-f105-4d87-9657-af3ae9e6032e/SRR16106088_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8b2b36fc-92a1-4746-93bb-050aa475bd2b?catalog=dcp28&version=2022-04-07T19%3A27%3A34.435000Z"
output="38dedfdf-d9f5-4e8c-b49a-58960a26b9f0/SRR16105939_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2d1f87c8-8005-4568-9fb3-4d08758a9c60?catalog=dcp28&version=2022-04-07T19%3A27%3A29.262000Z"
output="fa0de6b6-c530-4a21-b41d-ca8c94299717/SRR16105896_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fdb2cdd3-aaa2-4990-a90c-11807258c570?catalog=dcp28&version=2022-04-07T19%3A27%3A44.949000Z"
output="55afffb6-c0a9-451f-9a72-21dc328340ae/SRR16105974_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9dfa817e-059e-4315-b581-512547a6c297?catalog=dcp28&version=2022-04-07T19%3A27%3A03.868000Z"
output="339859d9-009d-4f94-9a39-5e1e79108ec8/SRR16105831_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2d6e98b1-f918-4249-8a3f-8b411225fe9f?catalog=dcp28&version=2022-04-07T19%3A27%3A32.759000Z"
output="cdd8b7fe-4206-4fb5-82b1-cf6ef8973cc4/SRR16105926_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/22fafe8b-d2e0-4560-95db-8c0b1d774eac?catalog=dcp28&version=2022-04-07T19%3A27%3A55.484000Z"
output="c7d75ede-9c9a-483c-8695-8bea63ab971b/SRR16106004_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8c848e5b-e1a5-46a1-a3db-6ca366f2711a?catalog=dcp28&version=2022-04-07T19%3A27%3A33.041000Z"
output="1e46ffa8-1729-4729-8957-4d2dead9399d/SRR16105929_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1376c5d3-1ac8-42e7-b5c1-75c7e79eb7aa?catalog=dcp28&version=2022-04-07T19%3A27%3A21.508000Z"
output="70a8b043-6ba0-499c-bcc5-37853b13d405/SRR16105881_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b0fbcf7a-44f7-4eae-bca6-458829f468ce?catalog=dcp28&version=2022-04-07T19%3A26%3A57.400000Z"
output="7d5b2f88-b0d0-479d-b96d-405377fc61df/SRR16105784_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08660aaf-9d04-45ec-8665-6c51a36df623?catalog=dcp28&version=2022-04-07T19%3A28%3A00.362000Z"
output="cf3ffb3a-7ea2-4266-b4db-5fa6c850e5b2/SRR16106035_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ff277c6f-ca58-4f33-a727-9535632434b2?catalog=dcp28&version=2022-04-07T19%3A28%3A11.301000Z"
output="aea32034-1c9e-424e-a932-1d45afc2708d/SRR16106093_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f6fcd55b-5620-4af0-bf7d-7232d4dc37db?catalog=dcp28&version=2022-04-07T19%3A26%3A56.300000Z"
output="1a23c808-8cdd-48db-981a-1f5c2c12f8af/SRR16105762_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7a339127-8b98-4dfa-ba17-3657dfcd64bd?catalog=dcp28&version=2022-04-07T19%3A27%3A45.778000Z"
output="28a66651-a897-4185-98a5-001e4b15e6c8/SRR16105979_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d8318912-ef07-4ba6-a2f5-6de91f6ac80f?catalog=dcp28&version=2022-04-07T19%3A27%3A57.972000Z"
output="d8d16e5f-217e-4d25-83b2-b2dbf921c590/SRR16106029_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ead3026c-e708-44cc-9520-90cc9d6bc97d?catalog=dcp28&version=2022-04-07T19%3A27%3A32.402000Z"
output="06fb0d09-a800-40b6-838d-1c20d78ecbdc/SRR16105923_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3c908be7-253e-4650-a40d-a7784bd78cbd?catalog=dcp28&version=2022-04-07T19%3A27%3A44.221000Z"
output="7bc17c14-2014-4e70-aaaf-19d5d9a6e75e/SRR16105967_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/940a6049-5379-45b1-b78e-5711b346eee3?catalog=dcp28&version=2022-04-07T19%3A27%3A59.594000Z"
output="aee6026d-07c1-47f7-b443-b31d4ddf4e26/SRR16106034_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/25df148a-8400-4779-91ab-a54c6b791503?catalog=dcp28&version=2022-04-07T19%3A27%3A30.786000Z"
output="9fd8eb0e-290d-45c0-b383-31370e729e8f/SRR16105911_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c2af3e16-4480-44ca-b765-a396e4551da6?catalog=dcp28&version=2022-04-07T19%3A26%3A58.781000Z"
output="23ef0a1d-b646-4c01-8959-f8af1070e46f/SRR16105812_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3b0e7e1a-ec28-40a8-8afd-23fc7f62bed2?catalog=dcp28&version=2022-04-07T19%3A27%3A08.801000Z"
output="ae48556e-60dc-4ad4-9096-e2421da4586c/SRR16105836_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e5971577-f09f-4977-9426-21214d925dd9?catalog=dcp28&version=2022-04-07T19%3A28%3A11.276000Z"
output="aea32034-1c9e-424e-a932-1d45afc2708d/SRR16106093_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c01d5bc9-fe8a-4409-8527-83ada692a6fb?catalog=dcp28&version=2022-04-07T19%3A26%3A59.236000Z"
output="eb093031-aedd-4fa6-a5cc-b380e928ac34/SRR16105821_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08d8ed7e-e13b-481b-bc3e-364f2760a256?catalog=dcp28&version=2022-04-07T19%3A28%3A09.779000Z"
output="de74d25d-e2c1-4c5e-9315-a13281938e7f/SRR16106080_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e25a9939-d4a5-4f1a-80c5-4b73a0941a18?catalog=dcp28&version=2022-04-07T19%3A27%3A31.642000Z"
output="3ea625cc-c21a-4dd4-a6b3-4ef07dd06fe5/SRR16105914_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2ff95e59-bdd4-4f03-8552-4311100576eb?catalog=dcp28&version=2022-04-07T19%3A28%3A12.337000Z"
output="bc8373a3-3f43-4498-b083-7eca3f757c69/SRR16106107_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b4a2b074-3c42-478b-a2af-7ad3c68915f2?catalog=dcp28&version=2022-04-07T19%3A28%3A00.578000Z"
output="f28f7f6f-87b3-48ca-b441-b24447ef1f58/SRR16106036_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ba31c22f-e717-42da-8f23-e44e147d9481?catalog=dcp28&version=2022-04-07T19%3A26%3A59.719000Z"
output="6c902c8d-c727-4e3b-a2fa-fd8a09df9f31/SRR16105826_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/42e6652a-a9e1-4492-b1db-98426a56190b?catalog=dcp28&version=2022-04-07T19%3A27%3A29.820000Z"
output="5320df1a-9714-439c-85ea-f23d57ba9c5a/SRR16105901_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fc8cf8a2-d676-4c31-a392-39926fbdb9ba?catalog=dcp28&version=2022-04-07T19%3A26%3A58.557000Z"
output="cfe1f1f6-6e1f-46d4-85ed-e516440be211/SRR16105808_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f90fe712-8323-4ca7-82eb-48184b7e6c13?catalog=dcp28&version=2022-04-07T19%3A27%3A44.257000Z"
output="7bc17c14-2014-4e70-aaaf-19d5d9a6e75e/SRR16105967_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f92f8072-34b8-49a6-b33a-d97cbb37c070?catalog=dcp28&version=2022-04-07T19%3A27%3A20.050000Z"
output="ff4c95fb-f0d3-4f3c-a147-37f48b2040b0/SRR16105871_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d5c6332c-e993-493d-8342-a9488b015116?catalog=dcp28&version=2022-04-07T19%3A27%3A15.642000Z"
output="91b3a074-511b-46f5-a745-6a020ba66cda/SRR16105840_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e1b3708b-5dec-457d-b82a-5cd333f00f2f?catalog=dcp28&version=2022-04-07T19%3A27%3A37.987000Z"
output="14972570-4961-433f-8ad2-a08faf27941f/SRR16105944_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/01f243ee-7df7-4a4a-98f8-5f17d9233adf?catalog=dcp28&version=2022-04-07T19%3A27%3A56.797000Z"
output="9e497c89-2ba7-4422-8cdb-28a93eea8766/SRR16106015_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5e0d0d99-34e0-41b1-9102-673f51634173?catalog=dcp28&version=2022-04-07T19%3A28%3A08.617000Z"
output="acc0fc8c-a1d8-48c5-a6a1-f5cc80ef5e5e/SRR16106063_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/135c6ee6-3862-429d-b207-d4fc7bdd922a?catalog=dcp28&version=2022-04-07T19%3A27%3A31.762000Z"
output="1c4fe4d7-ac3c-4cb8-befc-d84b3990091f/SRR16105916_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/023cb903-001e-4246-aca3-1b2713df3bc3?catalog=dcp28&version=2022-04-07T19%3A28%3A08.257000Z"
output="a1402ec5-dcbb-4fe0-84df-2d92e26273b9/SRR16106056_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/df30e9b2-43c8-4429-a00e-f8ca35cb4e04?catalog=dcp28&version=2022-04-07T19%3A27%3A57.635000Z"
output="7e85520c-1b32-440a-9296-f575ded6605d/SRR16106024_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d76a3354-1556-4c10-b9a6-aefd2c5878c1?catalog=dcp28&version=2022-04-07T19%3A26%3A58.355000Z"
output="7bec011d-f68f-4825-857b-e3a25b76891e/SRR16105805_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5fb7c6d8-1c14-4dd4-943f-0075b999f436?catalog=dcp28&version=2022-04-07T19%3A28%3A08.547000Z"
output="d1be7ef7-8edb-4dd0-be00-4692a569dff0/SRR16106061_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b1243956-1d2a-45dd-8e3c-5d2432086077?catalog=dcp28&version=2022-04-07T19%3A26%3A56.425000Z"
output="9205f192-10b9-4044-be8b-ed22fac9c1dd/SRR16105764_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a82d6af1-3b55-4065-9417-c061cd7ebead?catalog=dcp28&version=2022-04-07T19%3A28%3A08.858000Z"
output="1412c4b9-44a5-4ac4-9601-e71d23c1f949/SRR16106068_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d173dae0-e9b6-4d75-8f59-3ce3d0d055d6?catalog=dcp28&version=2022-04-07T19%3A27%3A29.791000Z"
output="5320df1a-9714-439c-85ea-f23d57ba9c5a/SRR16105901_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c804358c-11a4-4284-a1ab-16c574bfdd1d?catalog=dcp28&version=2022-04-07T19%3A27%3A55.404000Z"
output="c7d75ede-9c9a-483c-8695-8bea63ab971b/SRR16106004_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0df00bce-4f60-4769-a33f-5464f7b41d28?catalog=dcp28&version=2022-04-07T19%3A28%3A08.157000Z"
output="bb90f392-7e94-4cc6-b11c-8ed6b9e16dde/SRR16106055_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/14524b15-58ac-4ab4-b54c-579342a631e0?catalog=dcp28&version=2022-04-07T19%3A27%3A54.873000Z"
output="bd7283e6-4da2-4c55-967d-ff0d1c0bd59f/SRR16106001_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/879e1a0b-c98d-4d9b-b438-b0dde3e65b8b?catalog=dcp28&version=2022-04-07T19%3A27%3A21.338000Z"
output="750ee074-c01f-4378-bea9-53e746bf1b07/SRR16105879_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/11f457d4-5114-40d5-aeb7-a86370b72c99?catalog=dcp28&version=2022-04-07T19%3A28%3A10.059000Z"
output="15e70126-0d04-40a3-b1bd-939bf7890b2f/SRR16106084_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c5bc3e66-039b-49b2-94e1-0ebf02cb13d9?catalog=dcp28&version=2022-04-07T19%3A27%3A57.088000Z"
output="70b8c2de-d4e3-492c-993b-101ff35d4f7c/SRR16106017_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2b1e1a59-2918-4ad9-b337-210dfe773913?catalog=dcp28&version=2022-04-07T19%3A28%3A11.636000Z"
output="f5395a3a-99ca-426e-8e85-9264afd5b3e8/SRR16106098_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e9a91757-2f05-44b3-a84b-5b3626d1d453?catalog=dcp28&version=2022-04-07T19%3A26%3A57.446000Z"
output="1cc5a3bc-db79-481b-9a57-8f0683c3ae1a/SRR16105785_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b17fd2bc-f3d3-4466-923f-29fbab52567e?catalog=dcp28&version=2022-04-07T19%3A26%3A56.046000Z"
output="d92fea69-f5b7-4609-9f51-54328b3e0e14/SRR16105755_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a82c8a9a-1ae8-48a6-b66f-4c08200ef546?catalog=dcp28&version=2022-04-07T19%3A27%3A02.297000Z"
output="175d983d-e177-44a6-9bcf-dbc121e48b0b/SRR16105829_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/120a37b5-8725-4c63-9243-612122b5d210?catalog=dcp28&version=2022-04-07T19%3A27%3A31.582000Z"
output="3ea625cc-c21a-4dd4-a6b3-4ef07dd06fe5/SRR16105914_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08b286a7-d451-4e12-ad6f-00f1dbc4dd72?catalog=dcp28&version=2022-04-07T19%3A26%3A57.194000Z"
output="2407f163-90e5-4aad-8944-837e4f541a74/SRR16105780_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9593b408-f73b-4a0a-809f-c50b8756be7c?catalog=dcp28&version=2022-04-07T19%3A26%3A58.848000Z"
output="a6c579bc-a1fd-4e2f-8848-d7fa40ecada9/SRR16105813_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7ecb0896-0f6a-4c71-bf96-bc6f7873804c?catalog=dcp28&version=2022-04-07T19%3A27%3A12.076000Z"
output="8f305642-c861-49fb-a8d0-05b3ef0396f8/SRR16105837_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c5ae483a-5496-426f-b0b3-f74f5ba87a7b?catalog=dcp28&version=2022-04-07T19%3A27%3A20.832000Z"
output="6d41648e-e6bb-4b77-924f-beae862055d0/SRR16105875_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/98fdd0e2-abad-454f-8240-92874b9a517a?catalog=dcp28&version=2022-04-07T19%3A28%3A08.506000Z"
output="3b67a2e3-8952-4d16-8cef-4318535b0cce/SRR16106060_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/06f1f199-cf08-40ee-a38c-6762e63de885?catalog=dcp28&version=2022-04-07T19%3A26%3A56.740000Z"
output="e7f33f30-581f-4a1d-be0c-1520c6ec60f2/SRR16105773_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4aaa46df-7044-41ed-9cbe-d08264cc704c?catalog=dcp28&version=2022-04-07T19%3A27%3A35.599000Z"
output="ba6d0a59-079c-4cac-8d44-1777c77d2e07/SRR16105940_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ddf08af5-692b-4e63-9053-9a335858e30b?catalog=dcp28&version=2022-04-07T19%3A27%3A32.718000Z"
output="cdd8b7fe-4206-4fb5-82b1-cf6ef8973cc4/SRR16105926_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0a1c8e9d-3e80-4e7e-a102-856e44257eb6?catalog=dcp28&version=2022-04-07T19%3A28%3A00.397000Z"
output="cf3ffb3a-7ea2-4266-b4db-5fa6c850e5b2/SRR16106035_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6a18673d-b1a4-4295-b9d1-d12221f12165?catalog=dcp28&version=2022-04-07T19%3A27%3A54.373000Z"
output="a50015b5-0ec1-4950-acf2-be9b5873b98e/SRR16105996_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/38d5d129-70ad-4803-b025-b6608bf2d582?catalog=dcp28&version=2022-04-07T19%3A27%3A42.866000Z"
output="998ae609-7c67-4ff9-afe7-bfd518484e60/SRR16105956_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/be5411e5-1c6f-45d8-b927-0c8702c9f782?catalog=dcp28&version=2022-04-07T19%3A27%3A55.972000Z"
output="b1211531-2be2-448b-b806-e137b07d779c/SRR16106008_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/261a24af-268f-4e75-a005-d812edd770ac?catalog=dcp28&version=2022-04-07T19%3A26%3A57.157000Z"
output="f2eac87b-df1f-4620-ae7d-69d4a36700d3/SRR16105779_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4b03da5c-4d74-4c3a-a476-7d2d178d6415?catalog=dcp28&version=2022-04-07T19%3A26%3A58.422000Z"
output="3784dc2a-7ff3-4a2a-901e-5041b47f1af0/SRR16105807_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e0509b8a-beab-4ffb-bb05-d94457a7877c?catalog=dcp28&version=2022-04-07T19%3A27%3A32.815000Z"
output="b42b17c1-f6c8-4ec5-a4de-0373439e383f/SRR16105927_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1d5a830a-d5a6-4213-99c1-a5a79ecf3328?catalog=dcp28&version=2022-04-07T19%3A27%3A54.739000Z"
output="b9e3f9f0-8005-4355-ae10-20bc84286c6c/SRR16105999_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7d3380dd-6ea4-43c6-a6ea-bea5a532b47a?catalog=dcp28&version=2022-04-07T19%3A28%3A08.800000Z"
output="4a6953e5-a40a-4cda-a577-7c48a070d84b/SRR16106067_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a4782c25-adb2-467f-a2cb-1b301cf8e32b?catalog=dcp28&version=2022-04-07T19%3A26%3A56.616000Z"
output="6190457d-00eb-41cb-b11e-c6e06604f58f/SRR16105769_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/02b6e1d2-fbbc-415d-9fe2-694120147e24?catalog=dcp28&version=2022-04-07T19%3A28%3A08.708000Z"
output="2200a288-6638-4165-89b7-1bd117e66617/SRR16106065_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3dfa5a06-f40d-4809-8775-7533b8d2da64?catalog=dcp28&version=2022-04-07T19%3A27%3A37.230000Z"
output="f9b2dc8e-6b3c-458d-aac8-85d19e019c0a/SRR16105942_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/84b6a63f-4f91-4c20-9972-04823680cd5b?catalog=dcp28&version=2022-04-07T19%3A26%3A59.623000Z"
output="237910d7-064b-491a-b077-2c4ee7c52708/SRR16105825_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/618d6a47-672e-4476-93d4-07c4b37372f5?catalog=dcp28&version=2022-04-07T19%3A27%3A17.594000Z"
output="ac86fd53-27a1-415f-9aa4-1889967604cc/SRR16105854_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fbc3c851-9544-436b-8b38-df8589053bfe?catalog=dcp28&version=2022-04-07T19%3A27%3A02.433000Z"
output="f3c78381-3d38-4a08-9532-1abfb93d0897/SRR16105830_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bbe3c88d-97fc-4654-ba1c-8eb242599efc?catalog=dcp28&version=2022-04-07T19%3A28%3A11.949000Z"
output="7b142e78-0ab7-40c0-9b1b-0ffe9ecf0582/SRR16106102_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f503b5ef-165b-4f5a-918c-2a342f6e064b?catalog=dcp28&version=2022-04-07T19%3A26%3A57.594000Z"
output="cfc0992e-1b03-434d-a5d4-663b0b5bc95f/SRR16105789_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/64e5c241-991d-48cd-b610-c8739584c91d?catalog=dcp28&version=2022-04-07T19%3A27%3A32.583000Z"
output="3e6f7d88-6ab6-4dfd-b4f2-1371411780a7/SRR16105924_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5ff4aecb-a9dc-4774-8554-49a90f0a000d?catalog=dcp28&version=2022-04-07T19%3A26%3A57.582000Z"
output="cfc0992e-1b03-434d-a5d4-663b0b5bc95f/SRR16105789_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/44112dbe-b696-4862-a5ba-36bb9693c1b9?catalog=dcp28&version=2022-04-07T19%3A27%3A56.290000Z"
output="91db17aa-c64d-4dd1-abb1-7a7301c6dfe5/SRR16106010_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9cfabff6-e881-4877-863b-4bdfbb9362d2?catalog=dcp28&version=2022-04-07T19%3A26%3A57.082000Z"
output="011d1060-e572-4124-b96e-cf3d8acd3016/SRR16105778_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3e57539f-934e-499c-a708-23fcf624568c?catalog=dcp28&version=2022-04-07T19%3A27%3A20.255000Z"
output="eede025d-bdd4-46d4-866c-f5127bd7b177/SRR16105872_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/924cd9d5-c249-446c-8396-0ec792ecd592?catalog=dcp28&version=2022-04-07T19%3A27%3A43.661000Z"
output="b053b90f-9396-4c5d-ae9d-76876452d688/SRR16105962_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b3d8f699-5e9e-419d-a635-ee3b876a3acd?catalog=dcp28&version=2022-04-07T19%3A27%3A58.001000Z"
output="d8d16e5f-217e-4d25-83b2-b2dbf921c590/SRR16106029_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3f3b9e2c-5cff-4de8-91b9-01016708ba47?catalog=dcp28&version=2022-04-07T19%3A27%3A16.829000Z"
output="db5cb49d-1ce9-4ffc-b4fb-38b260573409/SRR16105849_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3fadde2f-af0b-43a3-9253-369d8845a692?catalog=dcp28&version=2022-04-07T19%3A27%3A15.850000Z"
output="91b3a074-511b-46f5-a745-6a020ba66cda/SRR16105840_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b37d9cd1-9727-4446-b176-6ea5f6567223?catalog=dcp28&version=2022-04-07T19%3A27%3A19.598000Z"
output="7cae2684-20ec-4295-9010-46d6ab358dee/SRR16105867_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8fd111c3-f92b-40a7-8d5d-1438296a0da9?catalog=dcp28&version=2022-04-07T19%3A27%3A19.674000Z"
output="1d66e5bd-d41e-47c2-b825-8ca45d02813f/SRR16105868_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b323fd35-4cd0-4a0d-b8b7-d4e08750d3bd?catalog=dcp28&version=2022-04-07T19%3A28%3A11.316000Z"
output="aea32034-1c9e-424e-a932-1d45afc2708d/SRR16106093_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ce4a4cb1-dd2b-4a69-be27-8ef15eb16713?catalog=dcp28&version=2022-04-07T19%3A27%3A54.853000Z"
output="c9f2e14f-f0fb-4f6a-90cd-2ab1aa22938e/SRR16106000_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ddd555ea-9fa8-4952-8eb7-c8133a36c6ac?catalog=dcp28&version=2022-04-07T19%3A27%3A33.237000Z"
output="86b2c520-0be0-499c-8394-efecce2ae800/SRR16105931_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ab249131-878b-4639-b852-fe438818e231?catalog=dcp28&version=2022-04-07T19%3A27%3A57.613000Z"
output="7e85520c-1b32-440a-9296-f575ded6605d/SRR16106024_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fba23ce4-da0a-48e1-a3f8-8668d7263225?catalog=dcp28&version=2022-04-07T19%3A27%3A18.482000Z"
output="cf82af2c-ab88-4b88-8211-679f41f97abc/SRR16105862_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bc997e6a-85fa-4692-a41a-ad123f427e40?catalog=dcp28&version=2022-04-07T19%3A27%3A43.206000Z"
output="37a8cdd4-737e-412f-9a42-5c8ea15a7745/SRR16105960_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/40469d86-28d2-4a12-8b90-3fbad84e21a0?catalog=dcp28&version=2022-04-07T19%3A27%3A20.459000Z"
output="d0641426-1fc5-42ac-815f-604ddad42dfc/SRR16105873_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/46b8d778-026b-42b7-9dda-9f660bc4ecac?catalog=dcp28&version=2022-04-07T19%3A26%3A57.333000Z"
output="5e801b90-8c49-44b3-b703-9a5b073f07a5/SRR16105783_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/80cfc673-6983-48a9-b613-46b3d573dd22?catalog=dcp28&version=2022-04-07T19%3A26%3A57.570000Z"
output="cfc0992e-1b03-434d-a5d4-663b0b5bc95f/SRR16105789_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/302a8a14-f2c9-406c-a846-cef143709e17?catalog=dcp28&version=2022-04-07T19%3A27%3A32.958000Z"
output="1e46ffa8-1729-4729-8957-4d2dead9399d/SRR16105929_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/aed49c99-2957-414b-9e7a-b0d5cf6e0ee8?catalog=dcp28&version=2022-04-07T19%3A27%3A56.623000Z"
output="4f14f89d-2083-4b95-b5b2-10e20b80484b/SRR16106013_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ded7b835-2467-4c56-af7d-1df64bd3c993?catalog=dcp28&version=2022-04-07T19%3A26%3A59.892000Z"
output="2629e260-5903-478b-a39e-59708cf2052f/SRR16105827_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/18a9fc62-ea4f-426a-ba8f-4407b6c07103?catalog=dcp28&version=2022-04-07T19%3A28%3A08.871000Z"
output="1412c4b9-44a5-4ac4-9601-e71d23c1f949/SRR16106068_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/41b65075-3fc6-4cd4-95a0-6eddb67dc71b?catalog=dcp28&version=2022-04-07T19%3A27%3A43.594000Z"
output="4591937f-51c1-4e7b-984d-b5a831e72cfd/SRR16105961_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4d442cf1-1fe9-45cc-8399-20283aad357e?catalog=dcp28&version=2022-04-07T19%3A28%3A09.237000Z"
output="486e1aeb-5925-42cc-a134-0eed4120fa2b/SRR16106072_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9782e698-36bc-4f12-9cf2-2846347a7100?catalog=dcp28&version=2022-04-07T19%3A26%3A56.059000Z"
output="d92fea69-f5b7-4609-9f51-54328b3e0e14/SRR16105755_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/aaadcbfd-d162-4a74-b4bd-1723dc2c1e4f?catalog=dcp28&version=2022-04-07T19%3A27%3A43.999000Z"
output="1e4f8657-7fd1-446e-a0ac-0fe3c567b6be/SRR16105964_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/faed0f60-1163-4c7a-9734-f825480aa73f?catalog=dcp28&version=2022-04-07T19%3A27%3A33.938000Z"
output="68441aaf-1e11-4e56-b2b4-4823b0c61093/SRR16105938_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a6a627d3-86a8-4fb3-993d-ed39bcc8da33?catalog=dcp28&version=2022-04-07T19%3A28%3A08.603000Z"
output="a4492d4f-6494-4f6c-9e15-30ddec5d10da/SRR16106062_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/812cd5a1-6bf3-41da-868a-bf24762ca065?catalog=dcp28&version=2022-04-07T19%3A27%3A47.347000Z"
output="0af2f0eb-bfd7-4de7-984a-1fa5b2f0236a/SRR16105984_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/753f3a30-caf1-457d-888d-5282fabd5cbf?catalog=dcp28&version=2022-04-07T19%3A27%3A58.019000Z"
output="d8d16e5f-217e-4d25-83b2-b2dbf921c590/SRR16106029_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/846e787a-22d4-4bc4-b9fe-96aa5827e24e?catalog=dcp28&version=2022-04-07T19%3A27%3A42.843000Z"
output="998ae609-7c67-4ff9-afe7-bfd518484e60/SRR16105956_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f5a799d3-068e-4e12-910d-f7169e072e9b?catalog=dcp28&version=2022-04-07T19%3A26%3A57.921000Z"
output="5973faea-848d-407a-a249-85ba85264249/SRR16105794_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e44176b9-702b-4eb6-a99f-56b3aa36789d?catalog=dcp28&version=2022-04-07T19%3A28%3A12.425000Z"
output="714f1455-b491-4644-be6a-31331c89e459/SRR16106109_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/55427ad2-3a44-44e9-980c-3f60eb3e9b81?catalog=dcp28&version=2022-04-07T19%3A27%3A33.884000Z"
output="68441aaf-1e11-4e56-b2b4-4823b0c61093/SRR16105938_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ebe5c836-3374-499d-867e-85721bebc98b?catalog=dcp28&version=2022-04-07T19%3A28%3A09.216000Z"
output="486e1aeb-5925-42cc-a134-0eed4120fa2b/SRR16106072_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1f144034-d6d7-4ed8-8372-627e0dc72502?catalog=dcp28&version=2022-04-07T19%3A26%3A58.513000Z"
output="cfe1f1f6-6e1f-46d4-85ed-e516440be211/SRR16105808_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/662c5e06-c534-428a-aed9-8449d633a313?catalog=dcp28&version=2022-04-07T19%3A28%3A12.580000Z"
output="6cd2b7d8-56e9-4ea4-aee8-9eac4c8948d2/SRR16106114_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/afad0cdc-e00d-452b-a141-819c81e095e4?catalog=dcp28&version=2022-04-07T19%3A27%3A56.777000Z"
output="9e497c89-2ba7-4422-8cdb-28a93eea8766/SRR16106015_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/69f05c61-84b7-4b10-a687-b4c1a8105d2d?catalog=dcp28&version=2022-04-07T19%3A26%3A57.169000Z"
output="f2eac87b-df1f-4620-ae7d-69d4a36700d3/SRR16105779_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d8d05570-fbaa-41ac-b499-ef908b7b6c1c?catalog=dcp28&version=2022-04-07T19%3A28%3A08.723000Z"
output="2200a288-6638-4165-89b7-1bd117e66617/SRR16106065_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f7cffada-92eb-4197-a704-1615f211a1c7?catalog=dcp28&version=2022-04-07T19%3A27%3A20.083000Z"
output="ff4c95fb-f0d3-4f3c-a147-37f48b2040b0/SRR16105871_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bf0cdddc-2fbb-4a35-9290-e56107e43ffa?catalog=dcp28&version=2022-04-07T19%3A26%3A56.072000Z"
output="b02a047d-33bf-4a58-b920-2a296516f007/SRR16105756_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4d616c45-4b07-403e-873b-bc74c1b220e1?catalog=dcp28&version=2022-04-07T19%3A26%3A57.265000Z"
output="4f083e47-dc2d-4984-9f39-dbc062aa6ba5/SRR16105782_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/370c039c-20f5-4fb3-a8cd-437e89fc7cb2?catalog=dcp28&version=2022-04-07T19%3A27%3A18.052000Z"
output="398a6d0a-dd1f-4125-8508-8dbb0439b38e/SRR16105857_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2141ac1f-6af1-4200-8934-a27f6ad72c20?catalog=dcp28&version=2022-04-07T19%3A27%3A30.269000Z"
output="ba60e59f-5da9-4f60-bd15-4186281ce060/SRR16105906_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9586a8c6-c941-4401-ae15-1a4c135e1275?catalog=dcp28&version=2022-04-07T19%3A26%3A57.278000Z"
output="4f083e47-dc2d-4984-9f39-dbc062aa6ba5/SRR16105782_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/df1d0699-f5fd-465c-bc9d-354c698e2288?catalog=dcp28&version=2022-04-07T19%3A27%3A18.540000Z"
output="cf82af2c-ab88-4b88-8211-679f41f97abc/SRR16105862_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4963a177-d295-4855-a182-aa35365ef43e?catalog=dcp28&version=2022-04-07T19%3A27%3A33.146000Z"
output="70a9dad1-5a6b-42ec-b62e-43050327e97d/SRR16105930_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/536547a6-ecc9-4617-9317-0b94c86c4be0?catalog=dcp28&version=2022-04-07T19%3A26%3A57.534000Z"
output="51d16b92-563a-40eb-9ceb-d7338bd7de8b/SRR16105788_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/afb2fa49-a48c-4745-98eb-880f0802201f?catalog=dcp28&version=2022-04-07T19%3A26%3A58.128000Z"
output="e69d2b80-9131-4af7-addb-2403890cd6ab/SRR16105799_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e8acd0c4-912b-473e-9e99-996079ba1fe8?catalog=dcp28&version=2022-04-07T19%3A26%3A58.490000Z"
output="3784dc2a-7ff3-4a2a-901e-5041b47f1af0/SRR16105807_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6d133737-1fb4-4e62-9fe1-a2fb92e767d9?catalog=dcp28&version=2022-04-07T19%3A27%3A45.670000Z"
output="28a66651-a897-4185-98a5-001e4b15e6c8/SRR16105979_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cddba048-30bf-4bcb-baba-8d20f8346e5d?catalog=dcp28&version=2022-04-07T19%3A27%3A47.680000Z"
output="0af2f0eb-bfd7-4de7-984a-1fa5b2f0236a/SRR16105984_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/24cc18ea-1d93-40d8-9be3-e77dc3885fb0?catalog=dcp28&version=2022-04-07T19%3A27%3A27.867000Z"
output="59d9a2bd-f41c-4cb7-8d94-61d8ae1588f0/SRR16105888_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/20f1542c-513d-42be-a6a1-4c1c80652cf2?catalog=dcp28&version=2022-04-07T19%3A27%3A45.078000Z"
output="464b4273-1681-4613-87d3-822449fcd112/SRR16105975_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1276b2f4-ead6-4dcc-b4f1-d54c023a341d?catalog=dcp28&version=2022-04-07T19%3A26%3A57.811000Z"
output="f4f1f564-781d-46a4-93b1-098c0b919e29/SRR16105793_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/61613607-6658-4322-815b-dbb8eb0e3cc9?catalog=dcp28&version=2022-04-07T19%3A28%3A08.694000Z"
output="08071d5d-2e9b-4a07-886f-82427c40e755/SRR16106064_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8dc1912a-cdec-4712-b2ed-59906756e6df?catalog=dcp28&version=2022-04-07T19%3A26%3A59.366000Z"
output="92203ca9-480b-47c5-8f37-1137caa7a0f6/SRR16105822_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f4f39361-0620-4c66-a384-6bd157677aa0?catalog=dcp28&version=2022-04-07T19%3A27%3A44.762000Z"
output="ea019938-5ed2-4fcd-90f5-95067bd26636/SRR16105972_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2a8e7ba6-3fcc-45d9-b85a-1cbc24064fe0?catalog=dcp28&version=2022-04-07T19%3A28%3A09.268000Z"
output="486e1aeb-5925-42cc-a134-0eed4120fa2b/SRR16106072_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3db19d79-c6f0-4892-9086-06183126bdd7?catalog=dcp28&version=2022-04-07T19%3A26%3A58.089000Z"
output="88855126-fc0c-480f-822b-0ff3779c92bd/SRR16105798_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08858936-a1fb-42e9-92ad-c88bf54177a5?catalog=dcp28&version=2022-04-07T19%3A27%3A56.713000Z"
output="4b583b84-9081-4f94-b8af-bea5d27d46f9/SRR16106014_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/14f5a1bb-2b18-4d18-a5ce-11e9d7824385?catalog=dcp28&version=2022-04-07T19%3A27%3A21.078000Z"
output="13f4f451-c38a-48d8-945e-282e3f01c50d/SRR16105876_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1a522a04-c432-4777-ba1d-5bc394383a2d?catalog=dcp28&version=2022-04-07T19%3A28%3A11.455000Z"
output="5042b694-fa2c-45ca-a0ff-72fc2cfee83e/SRR16106095_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d77e6ca2-4c4f-4f4c-a631-201cd7790903?catalog=dcp28&version=2022-04-07T19%3A27%3A58.046000Z"
output="724a9e10-bb44-4a94-8a50-2ff9636d46b0/SRR16106030_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0ab8507d-f278-4a03-883b-81ac0706121d?catalog=dcp28&version=2022-04-07T19%3A28%3A09.476000Z"
output="d2749e92-59b1-4bf8-a5aa-bf79ab36a671/SRR16106075_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f8ce580f-bbbc-458d-a0b6-fcaf6c3d13fd?catalog=dcp28&version=2022-04-07T19%3A27%3A58.230000Z"
output="44681fe6-eb3e-4509-bc14-efc39eb0ee06/SRR16106032_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d5525330-3736-46b9-9018-ecdf341a895d?catalog=dcp28&version=2022-04-07T19%3A28%3A10.112000Z"
output="15e70126-0d04-40a3-b1bd-939bf7890b2f/SRR16106084_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7e1c47f7-fdd3-4919-90d8-6685ec38964d?catalog=dcp28&version=2022-04-07T19%3A26%3A57.017000Z"
output="bacaa9c2-8b2a-45a6-9d21-3554b24b3e95/SRR16105777_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a41850a7-d419-42f9-a229-10da266bf99e?catalog=dcp28&version=2022-04-07T19%3A26%3A56.525000Z"
output="26747c63-f381-4b99-9d8a-04d79f36e779/SRR16105767_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c343d125-7a4a-4273-9b6b-2be03025720f?catalog=dcp28&version=2022-04-07T19%3A27%3A21.045000Z"
output="13f4f451-c38a-48d8-945e-282e3f01c50d/SRR16105876_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1e655ed3-f742-477a-b538-1a56a2e611b2?catalog=dcp28&version=2022-04-07T19%3A27%3A31.909000Z"
output="df64c85a-8709-4400-b9e2-b43a86e206cc/SRR16105917_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1af05493-a6e3-4164-ac20-6a376f5cab83?catalog=dcp28&version=2022-04-07T19%3A27%3A16.965000Z"
output="1b104e22-8f01-4954-927f-adc907a91382/SRR16105850_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/39e45478-1658-4d5d-b5d7-d3076788fdb9?catalog=dcp28&version=2022-04-07T19%3A26%3A57.946000Z"
output="e8233a1f-f0b8-4d98-a128-c09fde49478c/SRR16105795_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/40d9d5b8-ec5b-4be3-a788-d919ebb6333c?catalog=dcp28&version=2022-04-07T19%3A26%3A55.967000Z"
output="00375e15-335c-4fe8-8ac1-dd456ef205bc/SRR16105753_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b791a364-14c3-4458-a7cc-43300cd4dd02?catalog=dcp28&version=2022-04-07T19%3A27%3A56.961000Z"
output="70b8c2de-d4e3-492c-993b-101ff35d4f7c/SRR16106017_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1e8c7463-5fd6-4f81-9878-8f12b7aed1b7?catalog=dcp28&version=2022-04-07T19%3A28%3A09.311000Z"
output="20efe407-47b3-4323-834f-33088f530e9f/SRR16106073_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bd2b99aa-c95b-4326-9b1b-364e9636bd7e?catalog=dcp28&version=2022-04-07T19%3A27%3A55.793000Z"
output="6a8bd0c5-b373-47fd-ac70-93d666ac6dd7/SRR16106006_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/afa97e8f-19df-4cdc-894b-6ecf633a8109?catalog=dcp28&version=2022-04-07T19%3A27%3A44.135000Z"
output="ac7679e6-c824-462c-b88c-3dc1f5b42b47/SRR16105966_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/854a6248-f9d2-417d-9d98-cf1e23b1ab30?catalog=dcp28&version=2022-04-07T19%3A28%3A12.230000Z"
output="44ffb286-e933-45fd-97bb-ed3ff996cd9d/SRR16106105_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/219b2582-96cf-493a-8562-52d87e61a52c?catalog=dcp28&version=2022-04-07T19%3A26%3A56.653000Z"
output="a678f0bd-c71d-4557-a524-90f6f0ec7f78/SRR16105770_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4ffa154c-d690-4b72-8f83-002f14532e55?catalog=dcp28&version=2022-04-07T19%3A27%3A56.754000Z"
output="4b583b84-9081-4f94-b8af-bea5d27d46f9/SRR16106014_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/529479e4-3bae-475c-87b0-f4feee58a11a?catalog=dcp28&version=2022-04-07T19%3A27%3A16.591000Z"
output="43acafb6-087d-4d7f-bf32-643c83723170/SRR16105846_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fe20986d-59e4-4071-b9fc-856c94e5a64c?catalog=dcp28&version=2022-04-07T19%3A27%3A29.582000Z"
output="1b25e304-4e6a-479c-bf73-cb5254b6e7db/SRR16105898_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e99baf11-ea85-4918-926a-edbd7d486c2e?catalog=dcp28&version=2022-04-07T19%3A26%3A57.462000Z"
output="c36bafbe-1e9d-46a6-9c6f-eedfb4a6f9be/SRR16105786_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ad4c7a01-b4f1-4b1f-948c-a12fb396ed8e?catalog=dcp28&version=2022-04-07T19%3A27%3A58.150000Z"
output="afdc8ee8-c0e7-4fa0-b870-6daa37d5df9f/SRR16106031_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9cc06e52-7bc4-45e6-836a-dc939cdd3259?catalog=dcp28&version=2022-04-07T19%3A28%3A08.521000Z"
output="3b67a2e3-8952-4d16-8cef-4318535b0cce/SRR16106060_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a24ac6eb-82af-4d2f-9869-548ebbfc90ba?catalog=dcp28&version=2022-04-07T19%3A27%3A17.654000Z"
output="967d1938-e695-43f5-ba5c-f4d796a9c84f/SRR16105855_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4a57c90f-a93a-41e5-bb90-a5f71fdc5086?catalog=dcp28&version=2022-04-07T19%3A27%3A33.478000Z"
output="6da8fa15-9c95-4099-b285-0b041745213c/SRR16105933_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bfad702d-6b68-451c-b685-bdfcfa2465a3?catalog=dcp28&version=2022-04-07T19%3A27%3A16.333000Z"
output="f1b5b32a-3d89-4982-8668-b5b387461278/SRR16105843_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/96b92371-1031-4aad-999f-da44bc899799?catalog=dcp28&version=2022-04-07T19%3A27%3A57.214000Z"
output="126091f4-7045-4a8c-9a21-4f5970252b90/SRR16106019_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a86dcc3c-821d-4fb4-bc80-686074a71db8?catalog=dcp28&version=2022-04-07T19%3A27%3A30.754000Z"
output="ac5c9c01-3124-42a5-8191-c76c8f5ee22b/SRR16105910_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/aebfbf53-55c1-4cda-bef6-45eeff11234d?catalog=dcp28&version=2022-04-07T19%3A28%3A03.234000Z"
output="d6ecb457-a871-41d5-b2de-92ba4fadf9ae/SRR16106045_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d7f291e6-3a15-4332-8e77-75815dffe769?catalog=dcp28&version=2022-04-07T19%3A28%3A12.629000Z"
output="7e3af873-a224-4f4f-8b19-85093eafe0fc/SRR16106115_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0d00f33e-04d4-4ca6-8530-7dfef53d3814?catalog=dcp28&version=2022-04-07T19%3A26%3A56.788000Z"
output="25d1cb64-8f8a-4593-a647-9a12bf33ca81/SRR16105774_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fc993316-c5ef-41e4-9f7a-3154b9ec1b62?catalog=dcp28&version=2022-04-07T19%3A27%3A29.714000Z"
output="e024c21f-2e54-45cf-9212-bcb34de475cb/SRR16105900_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a0d1a848-bf03-4b99-9449-dd7d06269be1?catalog=dcp28&version=2022-04-07T19%3A27%3A56.101000Z"
output="c5e014da-2cc7-448e-89eb-e0720cd21f61/SRR16106009_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3daac476-9f2e-407f-89ee-b5bec8997730?catalog=dcp28&version=2022-04-07T19%3A26%3A57.415000Z"
output="1cc5a3bc-db79-481b-9a57-8f0683c3ae1a/SRR16105785_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6dc3317d-a0f0-4c43-9a74-30a23a842c3c?catalog=dcp28&version=2022-04-07T19%3A27%3A30.609000Z"
output="efb14c76-39db-469e-857f-4785a686f671/SRR16105909_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/07e0c109-7f8c-46b5-954f-3685f7067e36?catalog=dcp28&version=2022-04-07T19%3A28%3A12.324000Z"
output="bc8373a3-3f43-4498-b083-7eca3f757c69/SRR16106107_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9d424519-1f27-4841-bd60-fdde67d0fcd9?catalog=dcp28&version=2022-04-07T19%3A26%3A57.619000Z"
output="1dd51ef1-5ba1-4931-81da-9b82bec052dd/SRR16105790_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/338b8764-0eb9-4dec-b232-1f6e105fe91e?catalog=dcp28&version=2022-04-07T19%3A26%3A58.156000Z"
output="8f5e7b77-9b95-4f02-b39b-6fd721cd2de0/SRR16105800_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/62ff0adf-9945-4962-a3a5-c7c17aef6d65?catalog=dcp28&version=2022-04-07T19%3A27%3A55.763000Z"
output="6a8bd0c5-b373-47fd-ac70-93d666ac6dd7/SRR16106006_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/143b086f-2d19-479f-940d-bfc9f8796d91?catalog=dcp28&version=2022-04-07T19%3A28%3A09.711000Z"
output="6d59dd5a-dbd4-4152-8b9d-c739413f7a21/SRR16106079_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/27383651-387f-4711-9224-2b229f1b69a9?catalog=dcp28&version=2022-04-07T19%3A28%3A08.679000Z"
output="08071d5d-2e9b-4a07-886f-82427c40e755/SRR16106064_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/17e5954c-55e4-4b70-b2ff-8c75e7befac8?catalog=dcp28&version=2022-04-07T19%3A27%3A54.836000Z"
output="c9f2e14f-f0fb-4f6a-90cd-2ab1aa22938e/SRR16106000_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a2924e6a-5649-45de-b1a6-1629336613b3?catalog=dcp28&version=2022-04-07T19%3A28%3A11.077000Z"
output="94662222-bc39-4187-870e-a1d467c95b98/SRR16106091_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5f4b10a1-f24d-43a9-be20-9144555c4f65?catalog=dcp28&version=2022-04-07T19%3A27%3A57.173000Z"
output="ef5f0bda-99b4-4dda-97bf-a986febb7166/SRR16106018_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0d998892-6141-4492-8c35-ad565ee871db?catalog=dcp28&version=2022-04-07T19%3A28%3A11.652000Z"
output="f5395a3a-99ca-426e-8e85-9264afd5b3e8/SRR16106098_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/48007549-bf00-4e79-b1af-4eb6ff79f136?catalog=dcp28&version=2022-04-07T19%3A27%3A57.812000Z"
output="8200dd65-0c24-403c-b5b5-f01fc24092d3/SRR16106026_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/91967342-ea8f-47db-a61b-347f809ad5d4?catalog=dcp28&version=2022-04-07T19%3A26%3A56.486000Z"
output="6ccb5aa6-da53-4de9-97ec-e0858905a2ce/SRR16105766_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/67a4d4d6-8a37-4341-8e58-746eea08db21?catalog=dcp28&version=2022-04-07T19%3A27%3A57.878000Z"
output="d5bc19e9-bd96-4e17-951c-d5edeaeb4d99/SRR16106027_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1394fcd1-a43b-41fd-a108-f92eec959928?catalog=dcp28&version=2022-04-07T19%3A28%3A08.630000Z"
output="acc0fc8c-a1d8-48c5-a6a1-f5cc80ef5e5e/SRR16106063_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/72ec3336-3d62-4180-bed6-c944cba0673e?catalog=dcp28&version=2022-04-07T19%3A27%3A02.709000Z"
output="f3c78381-3d38-4a08-9532-1abfb93d0897/SRR16105830_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/da69aa5d-e47e-4701-b87d-eb32e284c3fe?catalog=dcp28&version=2022-04-07T19%3A27%3A31.278000Z"
output="9d93665a-8355-41d3-bb89-e61678ad7437/SRR16105912_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c4e97f5d-799c-48be-9c3f-d1fa07971dc7?catalog=dcp28&version=2022-04-07T19%3A27%3A19.570000Z"
output="7cae2684-20ec-4295-9010-46d6ab358dee/SRR16105867_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/259afe65-8c6a-44e9-b344-544af103955a?catalog=dcp28&version=2022-04-07T19%3A27%3A45.364000Z"
output="69a82e8c-b336-48ba-aef6-d019a36b8152/SRR16105977_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6b3f5f7a-02c1-42e1-bf22-acfa0308739b?catalog=dcp28&version=2022-04-07T19%3A27%3A20.676000Z"
output="d674036d-63e5-4e71-8162-16c0fd41fc91/SRR16105874_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/31016821-08ca-48b9-876b-d11ef9638cf2?catalog=dcp28&version=2022-04-07T19%3A26%3A59.119000Z"
output="ff2f2a8c-422e-4866-a446-634ada3bc1b9/SRR16105818_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/75d1a948-b6a7-4928-97b5-174ae74f3b04?catalog=dcp28&version=2022-04-07T19%3A27%3A30.462000Z"
output="5fdc2a0f-c761-48fc-9204-402011d61a06/SRR16105908_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e670e0b0-b5bc-48e7-8192-23504093e2fe?catalog=dcp28&version=2022-04-07T19%3A28%3A09.151000Z"
output="e002d41a-66bf-47cf-9ff2-c5a18a2ac848/SRR16106071_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a8e9e6db-c33e-4223-bf67-ff5c8f88aec7?catalog=dcp28&version=2022-04-07T19%3A27%3A19.498000Z"
output="9ec75f26-f306-4ca5-a5d0-486fc7b5eb4e/SRR16105866_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/35ba91d6-5b22-42dc-85f0-ad891f0d7ffc?catalog=dcp28&version=2022-04-07T19%3A27%3A19.823000Z"
output="26bb8ffe-696d-4274-8a7d-dc494171b6bc/SRR16105869_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4caf30d8-d24a-43d7-a2fa-adc483ffc400?catalog=dcp28&version=2022-04-07T19%3A27%3A48.168000Z"
output="00ab3054-0713-4559-a30a-52622d79bee4/SRR16105985_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1b1a33ce-26b1-47ba-99c9-c34ac669dfe0?catalog=dcp28&version=2022-04-07T19%3A27%3A42.447000Z"
output="ec2cbf37-f90d-4b2b-9972-e2631e380027/SRR16105951_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/314adc02-e923-41da-be28-66ec4e803bcb?catalog=dcp28&version=2022-04-07T19%3A28%3A10.682000Z"
output="723d3641-f105-4d87-9657-af3ae9e6032e/SRR16106088_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d05d91d8-5f6e-46c4-9846-69deeaa30472?catalog=dcp28&version=2022-04-07T19%3A28%3A00.915000Z"
output="2fdb0a8d-4d67-48f7-947b-e377f91e3d6a/SRR16106040_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/45bb9b79-2c83-4f1d-a3b9-18db7e5104a2?catalog=dcp28&version=2022-04-07T19%3A27%3A28.622000Z"
output="83f7466d-c72b-48d7-ad03-652e5a4ecb2e/SRR16105892_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/69cf0a64-3003-4dcf-81be-47254e232673?catalog=dcp28&version=2022-04-07T19%3A28%3A08.299000Z"
output="524efc57-19c1-4878-b2a3-c360f140d4f9/SRR16106057_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6d683ff3-ffe2-4078-ac71-409a58706e9f?catalog=dcp28&version=2022-04-07T19%3A27%3A41.119000Z"
output="c71a8645-5e08-44c1-829c-b03d26855b48/SRR16105946_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d449913b-049d-47f5-958f-8ff14823e3bd?catalog=dcp28&version=2022-04-07T19%3A27%3A29.891000Z"
output="0b237b15-1e32-4961-b572-7d184b8eff7d/SRR16105902_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/60bbaac2-2f3d-4642-a669-57dc6a2e9955?catalog=dcp28&version=2022-04-07T19%3A27%3A28.128000Z"
output="f92ab2be-b16d-49d5-9dd6-64a53d44a5f8/SRR16105890_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5649fe4d-e33b-40fa-ab56-77bb238ea6d2?catalog=dcp28&version=2022-04-07T19%3A26%3A58.465000Z"
output="3784dc2a-7ff3-4a2a-901e-5041b47f1af0/SRR16105807_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b085e562-2242-4978-a6f2-45f13b595dca?catalog=dcp28&version=2022-04-07T19%3A26%3A59.192000Z"
output="d8c88a8a-45e9-48cb-9dee-529409a3e2f5/SRR16105820_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4fbe4ab4-ed7a-4060-9b11-bcfafa618916?catalog=dcp28&version=2022-04-07T19%3A27%3A42.303000Z"
output="a685b4b1-712e-4248-b180-ba4fff92e5d6/SRR16105949_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/94893a29-56d8-47ad-9aa6-545443496111?catalog=dcp28&version=2022-04-07T19%3A27%3A19.437000Z"
output="9ec75f26-f306-4ca5-a5d0-486fc7b5eb4e/SRR16105866_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/148d68d5-2e70-4b95-8505-5a8346de41f8?catalog=dcp28&version=2022-04-07T19%3A26%3A57.315000Z"
output="5e801b90-8c49-44b3-b703-9a5b073f07a5/SRR16105783_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f9e36fe5-5683-4bad-bd75-d1846c1ca19c?catalog=dcp28&version=2022-04-07T19%3A27%3A33.783000Z"
output="6f7164e9-6b31-4da1-bf25-e370a36247cd/SRR16105937_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f573001a-a27e-4a39-9bb8-d945e2bede3d?catalog=dcp28&version=2022-04-07T19%3A27%3A42.507000Z"
output="87b24f06-ecbe-4233-a1c8-ffc65f6cac25/SRR16105952_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1f50e3b3-5c71-4007-a9f0-d97468a22f1d?catalog=dcp28&version=2022-04-07T19%3A28%3A09.526000Z"
output="41020ffc-e697-4c52-8d49-b9b3984a4338/SRR16106076_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a96f3568-4c45-420a-8e8f-f327b725e64b?catalog=dcp28&version=2022-04-07T19%3A27%3A30.631000Z"
output="efb14c76-39db-469e-857f-4785a686f671/SRR16105909_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6ef2be89-4ae8-4c8a-ac09-5d90357f9209?catalog=dcp28&version=2022-04-07T19%3A28%3A08.459000Z"
output="23a81775-b60d-4b4b-827b-21342ee95740/SRR16106059_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2e349e7b-33ca-45a7-ba2e-de6c58fc7a0a?catalog=dcp28&version=2022-04-07T19%3A27%3A42.590000Z"
output="45ebc9fb-89e0-4bfa-9a27-56c915f6e58b/SRR16105953_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/60e27496-9a86-4071-b9c6-a6134a6cef2f?catalog=dcp28&version=2022-04-07T19%3A27%3A42.643000Z"
output="d9e39c80-264e-44ec-81fc-c86f430742c3/SRR16105954_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/faecb767-a6f4-4386-be29-8c1df4af2f25?catalog=dcp28&version=2022-04-07T19%3A27%3A30.199000Z"
output="9b1691c2-52da-45a0-abe4-5b6de8955aee/SRR16105905_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b973cedf-865f-4595-b089-86ef90cb0694?catalog=dcp28&version=2022-04-07T19%3A27%3A58.312000Z"
output="753505f6-8367-4199-86fb-1e8a806a25a4/SRR16106033_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2c5556f1-66c7-4a1f-bb66-49b216a5fe8a?catalog=dcp28&version=2022-04-07T19%3A27%3A16.254000Z"
output="f1b5b32a-3d89-4982-8668-b5b387461278/SRR16105843_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f9145fd7-5eec-4adc-9e33-e0431a92013a?catalog=dcp28&version=2022-04-07T19%3A27%3A52.655000Z"
output="16e9ea04-bc15-4d39-8bce-5ab6c3d1a773/SRR16105992_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3f25e15a-7282-4797-a4b6-a42a024f07ac?catalog=dcp28&version=2022-04-07T19%3A27%3A57.683000Z"
output="584cbf84-929a-4d8a-acd4-606ecff0694c/SRR16106025_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/15bb28cd-3c2d-4348-936e-0e0153d6edfd?catalog=dcp28&version=2022-04-07T19%3A27%3A19.743000Z"
output="26bb8ffe-696d-4274-8a7d-dc494171b6bc/SRR16105869_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c55cc161-1d17-4803-83e5-bcd6780f1252?catalog=dcp28&version=2022-04-07T19%3A28%3A08.561000Z"
output="d1be7ef7-8edb-4dd0-be00-4692a569dff0/SRR16106061_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/879d55e0-b7ee-4f9d-97d4-ee318c7aba46?catalog=dcp28&version=2022-04-07T19%3A27%3A12.784000Z"
output="8f305642-c861-49fb-a8d0-05b3ef0396f8/SRR16105837_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3dc2ea1d-944d-460f-b8e3-cedb5017a092?catalog=dcp28&version=2022-04-07T19%3A27%3A13.183000Z"
output="b6ff1eea-cb66-412d-94ce-57a04e83b50e/SRR16105838_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/533b76f9-796f-410f-9ced-4906d1fdd6c5?catalog=dcp28&version=2022-04-07T19%3A27%3A30.869000Z"
output="9fd8eb0e-290d-45c0-b383-31370e729e8f/SRR16105911_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/45260b76-b607-4874-b098-6fd8aa203414?catalog=dcp28&version=2022-04-07T19%3A28%3A11.996000Z"
output="7b142e78-0ab7-40c0-9b1b-0ffe9ecf0582/SRR16106102_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/151d21a9-7fc2-4bfa-abf9-4fc030ef8cc5?catalog=dcp28&version=2022-04-07T19%3A27%3A30.698000Z"
output="ac5c9c01-3124-42a5-8191-c76c8f5ee22b/SRR16105910_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c175fb2-0017-4b05-a1da-3f22125f486b?catalog=dcp28&version=2022-04-07T19%3A28%3A01.155000Z"
output="0f11ebc1-e6bc-4039-a9b5-74170fe9744f/SRR16106042_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2272cee0-d546-4789-acac-78c470824371?catalog=dcp28&version=2022-04-07T19%3A26%3A58.034000Z"
output="9db959a4-6dac-4d4b-8380-600e074699ff/SRR16105797_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/88e42d66-0772-4c66-bb85-2dac6a76d3d3?catalog=dcp28&version=2022-04-07T19%3A27%3A33.522000Z"
output="6c955fe5-cfc0-425c-942b-8f2ccd4139c5/SRR16105934_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ab1219ff-7ce9-4c15-b1e1-3a71cefa60c7?catalog=dcp28&version=2022-04-07T19%3A26%3A58.808000Z"
output="23ef0a1d-b646-4c01-8959-f8af1070e46f/SRR16105812_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/837d7537-729d-4430-88d8-903cba722e42?catalog=dcp28&version=2022-04-07T19%3A28%3A09.602000Z"
output="d56edd59-ff53-43c3-bc73-97d1b9fce3d2/SRR16106077_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fe40ff5b-4a7b-40ce-820c-72df289ba931?catalog=dcp28&version=2022-04-07T19%3A27%3A33.810000Z"
output="6f7164e9-6b31-4da1-bf25-e370a36247cd/SRR16105937_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/edc0712b-ab41-4c61-9011-b5e6cbbb4304?catalog=dcp28&version=2022-04-07T19%3A27%3A29.753000Z"
output="e024c21f-2e54-45cf-9212-bcb34de475cb/SRR16105900_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8a055467-c1f4-4e19-9484-6c57ada35daa?catalog=dcp28&version=2022-04-07T19%3A27%3A00.816000Z"
output="b7036c4e-fef5-4651-a427-f871763dfce3/SRR16105828_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f30cc725-3484-4df3-8cc4-117fdf2d7ff0?catalog=dcp28&version=2022-04-07T19%3A28%3A08.662000Z"
output="08071d5d-2e9b-4a07-886f-82427c40e755/SRR16106064_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0f0447d7-f2a7-4372-918e-0cda668ce91e?catalog=dcp28&version=2022-04-07T19%3A27%3A18.139000Z"
output="c89e1023-7a12-4f75-b097-617ae9cf0a4e/SRR16105858_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c8dfc6e8-ac81-412e-882a-7db9ca30cea5?catalog=dcp28&version=2022-04-07T19%3A28%3A08.478000Z"
output="23a81775-b60d-4b4b-827b-21342ee95740/SRR16106059_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8b416e51-8d85-45df-8374-c524d92aede2?catalog=dcp28&version=2022-04-07T19%3A26%3A58.115000Z"
output="e69d2b80-9131-4af7-addb-2403890cd6ab/SRR16105799_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5d6571d5-90e4-49fb-b287-c0bb71ed8b1b?catalog=dcp28&version=2022-04-07T19%3A28%3A10.031000Z"
output="949468a1-494e-4a3d-939d-03322e793ff0/SRR16106083_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a95cf1df-342d-4b1e-8713-4cfae08120c4?catalog=dcp28&version=2022-04-07T19%3A27%3A42.390000Z"
output="45a1481c-a462-4b18-9dd3-0bdf6ad981e0/SRR16105950_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/89c55188-002e-4e97-8bd1-08b64a00f61d?catalog=dcp28&version=2022-04-07T19%3A27%3A20.330000Z"
output="eede025d-bdd4-46d4-866c-f5127bd7b177/SRR16105872_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4985d9ae-b047-4f6a-9cc3-8c05193416a1?catalog=dcp28&version=2022-04-07T19%3A27%3A29.616000Z"
output="1b25e304-4e6a-479c-bf73-cb5254b6e7db/SRR16105898_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/06acedb6-9dab-4287-970d-caea66a0f72a?catalog=dcp28&version=2022-04-07T19%3A27%3A37.192000Z"
output="f9b2dc8e-6b3c-458d-aac8-85d19e019c0a/SRR16105942_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7de0c0bb-25ef-4276-af0c-987082765255?catalog=dcp28&version=2022-04-07T19%3A26%3A56.438000Z"
output="6bf6781c-1dd4-4f8a-a4c4-7314cbe642f0/SRR16105765_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5b85dc7a-3625-4ba7-83e6-8256fa4c293e?catalog=dcp28&version=2022-04-07T19%3A26%3A58.007000Z"
output="4f1b8e71-7586-4917-8831-f1229bb25c5a/SRR16105796_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c4a3f101-7164-47df-a562-acbe1bdb19d0?catalog=dcp28&version=2022-04-07T19%3A27%3A31.387000Z"
output="37646cd9-5845-4aa3-ba6a-d1cebddd0972/SRR16105913_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e859f4ea-932b-49f9-bad1-2637a870ced1?catalog=dcp28&version=2022-04-07T19%3A28%3A01.308000Z"
output="cd69f208-db53-4efd-a474-035ce10620a4/SRR16106043_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8a53b529-ca2b-4331-92a0-b886a34edd24?catalog=dcp28&version=2022-04-07T19%3A27%3A16.289000Z"
output="f1b5b32a-3d89-4982-8668-b5b387461278/SRR16105843_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f61ead4d-2c75-4e35-84bb-82c9f0e65315?catalog=dcp28&version=2022-04-07T19%3A27%3A31.666000Z"
output="20a8abe3-c25c-4736-a244-d66f6fd0ae91/SRR16105915_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4cf0a633-399a-47c8-864b-081d2eebfee1?catalog=dcp28&version=2022-04-07T19%3A28%3A07.630000Z"
output="d37506f9-06bc-4bb8-b71e-991af1edca45/SRR16106051_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5d182a6f-2bc7-4eec-91b3-96b72f486e10?catalog=dcp28&version=2022-04-07T19%3A27%3A37.259000Z"
output="f9b2dc8e-6b3c-458d-aac8-85d19e019c0a/SRR16105942_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d6d21b7c-14c9-4539-af10-ec25bad6e3dc?catalog=dcp28&version=2022-04-07T19%3A26%3A56.511000Z"
output="26747c63-f381-4b99-9d8a-04d79f36e779/SRR16105767_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d4671cf5-3fd1-4743-bb08-91cefa48a37a?catalog=dcp28&version=2022-04-07T19%3A27%3A56.466000Z"
output="40c1e501-6c42-4d72-9326-e698be1241b3/SRR16106011_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c7521c94-1f50-4714-ae40-087940e9ea14?catalog=dcp28&version=2022-04-07T19%3A28%3A11.052000Z"
output="d931e4f2-33e9-4233-9502-1dfd77a21d8c/SRR16106090_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/80baeab4-b6dd-4754-9640-12550b5268de?catalog=dcp28&version=2022-04-07T19%3A27%3A31.738000Z"
output="1c4fe4d7-ac3c-4cb8-befc-d84b3990091f/SRR16105916_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/33b4509f-7892-40ca-8cf9-6a3da0c8b086?catalog=dcp28&version=2022-04-07T19%3A27%3A54.398000Z"
output="a50015b5-0ec1-4950-acf2-be9b5873b98e/SRR16105996_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4b5a6792-4e45-41db-8ff9-8c99ab95799c?catalog=dcp28&version=2022-04-07T19%3A27%3A08.610000Z"
output="cd97de50-ba1b-42e3-ae2f-8e34a90eb766/SRR16105835_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/44e0a7e1-1f24-41ec-91c4-eba0a45f13cf?catalog=dcp28&version=2022-04-07T19%3A28%3A08.589000Z"
output="a4492d4f-6494-4f6c-9e15-30ddec5d10da/SRR16106062_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5653908f-7d46-4db3-bb0f-48aec8e8044c?catalog=dcp28&version=2022-04-07T19%3A28%3A11.559000Z"
output="cc0a9e54-c45e-4065-a662-fdeb71001fc6/SRR16106097_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/82464094-ec49-41c7-bd60-58a19e14ce17?catalog=dcp28&version=2022-04-07T19%3A28%3A11.873000Z"
output="e9b9cd07-16d8-442f-ba80-21afe8b98fad/SRR16106101_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/686d286a-f001-4e02-b898-7185f0be816e?catalog=dcp28&version=2022-04-07T19%3A27%3A19.985000Z"
output="92c8a58a-35fe-4b44-96ab-f6305dd8eaab/SRR16105870_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f7924418-8c2f-40a1-b722-998814642293?catalog=dcp28&version=2022-04-07T19%3A27%3A53.678000Z"
output="5937cfb9-d720-43c4-b41b-098489bde683/SRR16105993_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/02abd4c4-af50-46e8-ac79-c3a81c069329?catalog=dcp28&version=2022-04-07T19%3A27%3A19.766000Z"
output="26bb8ffe-696d-4274-8a7d-dc494171b6bc/SRR16105869_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ae74bea5-90cb-4f94-a0df-5e1a7b6a3c2b?catalog=dcp28&version=2022-04-07T19%3A26%3A58.394000Z"
output="ee1a5d8f-b801-4f53-8ef4-a2840105e89a/SRR16105806_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7d57b5e4-0c50-459a-ba90-65bed264e185?catalog=dcp28&version=2022-04-07T19%3A27%3A44.637000Z"
output="a94914ce-d6c7-4a6b-a581-94b6287c6980/SRR16105971_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/14545484-a7c6-40b3-895d-934671e95905?catalog=dcp28&version=2022-04-07T19%3A28%3A09.027000Z"
output="66ceee2f-7c84-458d-b713-bf74a8a93de7/SRR16106070_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5363d418-406c-4402-853f-f5bc32d58a9d?catalog=dcp28&version=2022-04-07T19%3A27%3A29.402000Z"
output="b4a55412-3273-4137-869f-68a93521fe25/SRR16105897_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/59fb5b10-cad7-4fd9-aa1c-0dc6e26f8081?catalog=dcp28&version=2022-04-07T19%3A26%3A58.143000Z"
output="8f5e7b77-9b95-4f02-b39b-6fd721cd2de0/SRR16105800_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f9589999-eeaf-40a8-bcc0-f56791fd9806?catalog=dcp28&version=2022-04-07T19%3A26%3A59.261000Z"
output="eb093031-aedd-4fa6-a5cc-b380e928ac34/SRR16105821_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/455de7aa-ebd4-4da6-b8cc-9b1c5f4bce8d?catalog=dcp28&version=2022-04-07T19%3A27%3A51.526000Z"
output="c5806b47-3a16-4319-baa2-dc014e981cb8/SRR16105991_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/68c1a575-b233-4438-8d70-c4e644978ac3?catalog=dcp28&version=2022-04-07T19%3A27%3A42.788000Z"
output="f97d049e-dcbd-4d1a-9349-704cd1edd1fb/SRR16105955_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/697863c3-b986-4543-9a78-69f580384cc3?catalog=dcp28&version=2022-04-07T19%3A26%3A58.303000Z"
output="34a12e21-0d7d-40e5-9e02-2e303ee76eed/SRR16105804_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b739a87b-c274-4ef2-8c57-81e11fdfd92d?catalog=dcp28&version=2022-04-07T19%3A26%3A57.606000Z"
output="1dd51ef1-5ba1-4931-81da-9b82bec052dd/SRR16105790_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/74b59b33-4a00-4932-b377-a565a2f3daad?catalog=dcp28&version=2022-04-07T19%3A28%3A08.023000Z"
output="aff1cdb9-840a-4f4b-8dbc-1a60620924da/SRR16106054_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dafb84b5-34c8-4c40-af41-e84c45db2cb2?catalog=dcp28&version=2022-04-07T19%3A27%3A17.262000Z"
output="74dbd63a-80a5-4cfd-b9d5-05a637ffc901/SRR16105851_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0b88fb1b-30f2-4cb5-827b-f7f23f829642?catalog=dcp28&version=2022-04-07T19%3A27%3A06.819000Z"
output="3ddbd8a5-3306-438c-a45f-a47f6315efd9/SRR16105833_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/31eb6284-e01d-4cb2-9d2b-d5677dbf76b5?catalog=dcp28&version=2022-04-07T19%3A27%3A27.214000Z"
output="e72d2857-7b4b-46aa-88c8-f4f5c63e7eb8/SRR16105884_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ae412472-8f7e-4d9f-bf30-c4dd16a1d403?catalog=dcp28&version=2022-04-07T19%3A27%3A33.077000Z"
output="1e46ffa8-1729-4729-8957-4d2dead9399d/SRR16105929_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c4294ccf-ff08-4700-9712-34a92b36afbd?catalog=dcp28&version=2022-04-07T19%3A28%3A00.757000Z"
output="5e12184a-b091-47a1-9db9-d9174f25dce8/SRR16106037_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b94d04db-5700-4774-8e25-f7598d630211?catalog=dcp28&version=2022-04-07T19%3A26%3A58.180000Z"
output="5d12037a-0a50-421c-84e0-367c12f41b55/SRR16105801_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/179a8633-2606-4f10-83ac-a4ea84ed126d?catalog=dcp28&version=2022-04-07T19%3A26%3A57.659000Z"
output="83b293d7-fd54-461f-ae45-4f228d3b63fb/SRR16105791_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ad879c74-aade-4a4a-b6cc-230d25020697?catalog=dcp28&version=2022-04-07T19%3A27%3A43.182000Z"
output="37a8cdd4-737e-412f-9a42-5c8ea15a7745/SRR16105960_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7f068bd1-0c75-4bf5-aa69-3f311974167f?catalog=dcp28&version=2022-04-07T19%3A27%3A58.282000Z"
output="44681fe6-eb3e-4509-bc14-efc39eb0ee06/SRR16106032_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a1eaca8b-bd07-4a83-a403-9c962fe71c60?catalog=dcp28&version=2022-04-07T19%3A27%3A30.168000Z"
output="9b1691c2-52da-45a0-abe4-5b6de8955aee/SRR16105905_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f327a45b-7084-42be-ab60-1f97c5dbdf59?catalog=dcp28&version=2022-04-07T19%3A27%3A56.486000Z"
output="60a8ac8a-d1f7-4521-98d8-a6d1f1d2f6d0/SRR16106012_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c9b06a1f-79b9-4506-b087-406325b033dd?catalog=dcp28&version=2022-04-07T19%3A27%3A44.427000Z"
output="bd3b5bfa-bb91-4a09-8737-67ac1da7af2f/SRR16105969_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/37fbdb13-df3b-4715-be61-3ec3e5079e52?catalog=dcp28&version=2022-04-07T19%3A28%3A09.365000Z"
output="2c9e75b6-f9fa-453f-9caa-e445e50c2e5d/SRR16106074_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b8e324da-27ed-4d20-a05e-7640fa9ab023?catalog=dcp28&version=2022-04-07T19%3A26%3A56.691000Z"
output="57e79970-7e14-43b7-8501-905f66922f9b/SRR16105771_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c1383de-e973-480c-afa1-3f267d7f1fbd?catalog=dcp28&version=2022-04-07T19%3A27%3A57.458000Z"
output="b668566d-5a0d-4839-a3f7-ba746f40ebfe/SRR16106022_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dcf584b6-1de2-4bcc-8340-1dd59bcd9ee0?catalog=dcp28&version=2022-04-07T19%3A27%3A55.592000Z"
output="608f4800-5e5f-4358-9043-c6bcd2b34562/SRR16106005_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/18b0c542-04db-4d24-b033-4e479cc29423?catalog=dcp28&version=2022-04-07T19%3A28%3A12.110000Z"
output="12d2463a-6951-430c-a01f-299db0e16b4b/SRR16106104_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c3b451f6-157c-40f4-a0d4-034491115f78?catalog=dcp28&version=2022-04-07T19%3A26%3A57.993000Z"
output="4f1b8e71-7586-4917-8831-f1229bb25c5a/SRR16105796_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/18ab50d9-a0f0-4a8a-8879-1d8d592cd21d?catalog=dcp28&version=2022-04-07T19%3A28%3A07.570000Z"
output="d37506f9-06bc-4bb8-b71e-991af1edca45/SRR16106051_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/de511580-72f4-4a94-a628-47aad987f7bd?catalog=dcp28&version=2022-04-07T19%3A27%3A29.134000Z"
output="f13ff253-8785-47e8-805a-1a5a08ae8345/SRR16105895_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/68a36d73-4088-4f7c-b71d-ad82a189e377?catalog=dcp28&version=2022-04-07T19%3A27%3A45.424000Z"
output="69a82e8c-b336-48ba-aef6-d019a36b8152/SRR16105977_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6be07c68-2797-4066-be35-0bd513a1ee7b?catalog=dcp28&version=2022-04-07T19%3A27%3A44.841000Z"
output="f575dc89-29eb-4c14-9951-03903f35551f/SRR16105973_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d9b3da02-c4de-4b75-9837-d9b1bfbc22f2?catalog=dcp28&version=2022-04-07T19%3A28%3A12.376000Z"
output="94316c6a-decf-400e-b9f1-9b2da2ee228c/SRR16106108_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/823582b6-7282-417b-b5e7-805d8d64510d?catalog=dcp28&version=2022-04-07T19%3A27%3A19.709000Z"
output="1d66e5bd-d41e-47c2-b825-8ca45d02813f/SRR16105868_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/53ede43f-7d8d-488c-87ef-6b0c4bfe036a?catalog=dcp28&version=2022-04-07T19%3A28%3A08.436000Z"
output="23a81775-b60d-4b4b-827b-21342ee95740/SRR16106059_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1e60f950-4e28-476c-9252-bbd021babef7?catalog=dcp28&version=2022-04-07T19%3A27%3A44.728000Z"
output="ea019938-5ed2-4fcd-90f5-95067bd26636/SRR16105972_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/33ecdde7-2995-4007-ab98-e1505a144bc8?catalog=dcp28&version=2022-04-07T19%3A27%3A56.181000Z"
output="c5e014da-2cc7-448e-89eb-e0720cd21f61/SRR16106009_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/95f447ea-efb6-4113-8cdb-7c3cab7e33b6?catalog=dcp28&version=2022-04-07T19%3A27%3A45.280000Z"
output="6d0e8144-c29c-456a-9d30-e62929af9f33/SRR16105976_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c67c903-2f0c-4b9b-bee0-6d47bd299900?catalog=dcp28&version=2022-04-07T19%3A28%3A03.771000Z"
output="e703efca-f439-45e7-989a-51e9219896b4/SRR16106046_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5974d7ed-3239-4112-8440-3407fa2b6079?catalog=dcp28&version=2022-04-07T19%3A27%3A27.798000Z"
output="59d9a2bd-f41c-4cb7-8d94-61d8ae1588f0/SRR16105888_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4920f6c0-3b84-4b05-95a9-b52b83c956e8?catalog=dcp28&version=2022-04-07T19%3A28%3A12.259000Z"
output="44ffb286-e933-45fd-97bb-ed3ff996cd9d/SRR16106105_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4f81bb55-17e3-4251-8de5-40f5d16b34b2?catalog=dcp28&version=2022-04-07T19%3A27%3A57.854000Z"
output="d5bc19e9-bd96-4e17-951c-d5edeaeb4d99/SRR16106027_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/95ab2596-26cf-43e4-8ed0-b8df0d4f8897?catalog=dcp28&version=2022-04-07T19%3A27%3A00.963000Z"
output="b7036c4e-fef5-4651-a427-f871763dfce3/SRR16105828_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c844630b-7ba8-4138-a8e7-1cfb89eaa45d?catalog=dcp28&version=2022-04-07T19%3A27%3A41.566000Z"
output="82ecaa87-aa59-455d-a17b-6a1b7a2c4409/SRR16105947_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2eb1ed03-ed84-46bc-bc09-ae9f28cc2d9b?catalog=dcp28&version=2022-04-07T19%3A28%3A00.873000Z"
output="54d67cd1-84f2-4b4a-bbe4-9b938cef55ee/SRR16106039_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e5ddfe75-7220-4c1d-940f-8913a86e4e3f?catalog=dcp28&version=2022-04-07T19%3A28%3A11.175000Z"
output="de4f5178-3b57-4791-ac2a-786a4768480c/SRR16106092_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/88840196-a655-4275-b07d-4da7347ebb32?catalog=dcp28&version=2022-04-07T19%3A27%3A33.265000Z"
output="86b2c520-0be0-499c-8394-efecce2ae800/SRR16105931_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c454215c-3daa-46b4-bd65-891662e70990?catalog=dcp28&version=2022-04-07T19%3A27%3A32.114000Z"
output="8de660b1-fa9e-48da-9d7d-ce171d684923/SRR16105920_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/922c200d-6622-48f1-92d1-d0913dbcbb15?catalog=dcp28&version=2022-04-07T19%3A26%3A59.346000Z"
output="92203ca9-480b-47c5-8f37-1137caa7a0f6/SRR16105822_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d1a8fddb-7be0-4f69-a79f-3df7bcc4dc0b?catalog=dcp28&version=2022-04-07T19%3A28%3A11.836000Z"
output="339fde68-d0a6-4e6d-bdca-9ef5cc084e34/SRR16106100_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/059f3af4-736f-417a-a468-edaa6eaaf0ef?catalog=dcp28&version=2022-04-07T19%3A27%3A29.635000Z"
output="81817ea5-b474-4514-b789-e593e7211b16/SRR16105899_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e7ce4818-9ad4-4092-a63e-143f1ef2c444?catalog=dcp28&version=2022-04-07T19%3A27%3A54.625000Z"
output="9923f38c-329a-40d1-956d-d0dd9ac70a66/SRR16105998_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a71d729b-f5e9-4bf5-ae5a-07c214a33d53?catalog=dcp28&version=2022-04-07T19%3A27%3A54.007000Z"
output="84d493d1-968f-4520-892d-3331d900b8f9/SRR16105995_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4b32c865-b9d6-48b2-8dd1-b97f3cf47125?catalog=dcp28&version=2022-04-07T19%3A27%3A19.406000Z"
output="9ec75f26-f306-4ca5-a5d0-486fc7b5eb4e/SRR16105866_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ccddb2ce-fb03-44c1-b3ed-a6a6fd8a37b2?catalog=dcp28&version=2022-04-07T19%3A28%3A06.939000Z"
output="0d7cc23a-8b6b-43a8-8621-4ba22fb36774/SRR16106049_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ff077b47-5ba3-4f80-8007-f47c8c467824?catalog=dcp28&version=2022-04-07T19%3A26%3A56.848000Z"
output="fe2e00d7-e6ff-4f11-a376-da60874a7924/SRR16105776_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9bfca576-6285-4cc6-a45f-9d3912117a45?catalog=dcp28&version=2022-04-07T19%3A27%3A46.114000Z"
output="636c619c-a2ec-4688-ba95-5990590fcc15/SRR16105983_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/604c142f-271d-4591-ab26-27337e8e8cb7?catalog=dcp28&version=2022-04-07T19%3A27%3A16.783000Z"
output="34898ed8-5e60-432c-b934-021842b4cfd8/SRR16105848_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cc0597ba-41e6-4c61-a3b0-13eeff29aeac?catalog=dcp28&version=2022-04-07T19%3A27%3A57.232000Z"
output="126091f4-7045-4a8c-9a21-4f5970252b90/SRR16106019_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d5f0d7a8-771b-4f04-ad14-81ac520ed83f?catalog=dcp28&version=2022-04-07T19%3A27%3A57.562000Z"
output="41fceb09-b7c8-40ce-b2d9-20eda5cbf63d/SRR16106023_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7192fc68-b9ca-4989-afc4-06d8b7c64ab9?catalog=dcp28&version=2022-04-07T19%3A27%3A00.614000Z"
output="b7036c4e-fef5-4651-a427-f871763dfce3/SRR16105828_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/431d21ce-975c-483a-a4ef-23f28d482c14?catalog=dcp28&version=2022-04-07T19%3A27%3A41.384000Z"
output="82ecaa87-aa59-455d-a17b-6a1b7a2c4409/SRR16105947_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0791a09c-c2fa-48ee-8373-765ba3352aab?catalog=dcp28&version=2022-04-07T19%3A27%3A29.857000Z"
output="0b237b15-1e32-4961-b572-7d184b8eff7d/SRR16105902_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2dbc84ba-bc32-4157-a9b2-667db65148f5?catalog=dcp28&version=2022-04-07T19%3A28%3A12.567000Z"
output="8a15abfd-b0db-4222-b59c-6032a0dced1a/SRR16106113_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/86ea3264-7d3e-4e92-9ade-01434483a1cd?catalog=dcp28&version=2022-04-07T19%3A28%3A11.504000Z"
output="c7c1d756-e4e9-4857-8c24-ba4eaafe9507/SRR16106096_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5ebbb7db-ead3-48dc-a6e4-b92bd9a1040b?catalog=dcp28&version=2022-04-07T19%3A27%3A18.268000Z"
output="d419844e-9a75-4f20-98a9-8c6b68b6e865/SRR16105860_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d06cc453-d093-4013-a30e-0599dd2771b0?catalog=dcp28&version=2022-04-07T19%3A27%3A42.103000Z"
output="37346a5a-99b2-465f-b0d4-1bba7616d547/SRR16105948_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5d3603d0-f92b-481a-95bc-39cf582f19bf?catalog=dcp28&version=2022-04-07T19%3A28%3A09.542000Z"
output="41020ffc-e697-4c52-8d49-b9b3984a4338/SRR16106076_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/97960dac-ba24-4e93-8ac4-10d422b13a4d?catalog=dcp28&version=2022-04-07T19%3A27%3A20.214000Z"
output="eede025d-bdd4-46d4-866c-f5127bd7b177/SRR16105872_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/19a1f305-83d6-4197-bfec-5bc428b7ad68?catalog=dcp28&version=2022-04-07T19%3A27%3A57.280000Z"
output="cff878d8-8e62-4686-b73d-2feaf2813300/SRR16106020_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8e7353c4-c4e2-42ba-963a-4334756e5cbf?catalog=dcp28&version=2022-04-07T19%3A27%3A37.290000Z"
output="d49f7948-f3c6-4fcd-8552-43d0e4ade6c1/SRR16105943_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dec1ef0a-860e-48f3-a545-afac1623350e?catalog=dcp28&version=2022-04-07T19%3A27%3A56.667000Z"
output="4b583b84-9081-4f94-b8af-bea5d27d46f9/SRR16106014_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7256d8cd-65c6-4dd0-ba73-868fb824377c?catalog=dcp28&version=2022-04-07T19%3A26%3A56.499000Z"
output="6ccb5aa6-da53-4de9-97ec-e0858905a2ce/SRR16105766_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f3859c3b-92ce-4fe7-a0b4-50d612ebf00a?catalog=dcp28&version=2022-04-07T19%3A27%3A31.870000Z"
output="df64c85a-8709-4400-b9e2-b43a86e206cc/SRR16105917_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2377f016-72ef-4a5b-bfe5-90dd40de446b?catalog=dcp28&version=2022-04-07T19%3A27%3A45.330000Z"
output="6d0e8144-c29c-456a-9d30-e62929af9f33/SRR16105976_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c49f0af2-1537-4b7c-b10e-a9ddb6051bf5?catalog=dcp28&version=2022-04-07T19%3A28%3A12.604000Z"
output="6cd2b7d8-56e9-4ea4-aee8-9eac4c8948d2/SRR16106114_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/721a08b7-0b9e-41ca-8bc0-c0f8aedc657f?catalog=dcp28&version=2022-04-07T19%3A27%3A54.699000Z"
output="b9e3f9f0-8005-4355-ae10-20bc84286c6c/SRR16105999_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5d389ae7-7225-42f2-9591-897cd57544a5?catalog=dcp28&version=2022-04-07T19%3A26%3A57.486000Z"
output="c36bafbe-1e9d-46a6-9c6f-eedfb4a6f9be/SRR16105786_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f7666d36-2244-4889-8889-9698f9eb200e?catalog=dcp28&version=2022-04-07T19%3A28%3A08.754000Z"
output="70abaeed-cb70-450c-9527-914ea48bf443/SRR16106066_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/eee6dcf6-8177-45d4-806a-bfd3fc81369d?catalog=dcp28&version=2022-04-07T19%3A27%3A16.669000Z"
output="75cb8029-0e19-47bb-a782-e9f4e89dfb09/SRR16105847_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a21a983c-313d-4bab-8d8e-30ae7fbdb783?catalog=dcp28&version=2022-04-07T19%3A27%3A32.884000Z"
output="8aeb0ebd-285a-424a-94b6-e9715786c1c2/SRR16105928_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6156f1c8-545a-48cf-b653-dfc7d56ad545?catalog=dcp28&version=2022-04-07T19%3A28%3A07.916000Z"
output="8af57556-1650-4217-a4e0-c76a67224a71/SRR16106053_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8ff6ef44-5515-4506-88be-aadfb49ee18a?catalog=dcp28&version=2022-04-07T19%3A28%3A08.830000Z"
output="4a6953e5-a40a-4cda-a577-7c48a070d84b/SRR16106067_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dec7154b-f535-4d1b-b4ad-4c75b142940f?catalog=dcp28&version=2022-04-07T19%3A27%3A28.653000Z"
output="83f7466d-c72b-48d7-ad03-652e5a4ecb2e/SRR16105892_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/73965a20-f17d-4542-b797-931aa757d6df?catalog=dcp28&version=2022-04-07T19%3A27%3A16.614000Z"
output="43acafb6-087d-4d7f-bf32-643c83723170/SRR16105846_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/64d76d84-3ab4-41ac-911e-ca5d0669f800?catalog=dcp28&version=2022-04-07T19%3A27%3A42.424000Z"
output="ec2cbf37-f90d-4b2b-9972-e2631e380027/SRR16105951_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bacf3ca9-5841-49d7-bf03-aa00cf925cfa?catalog=dcp28&version=2022-04-07T19%3A27%3A55.086000Z"
output="724c2f24-6739-40b4-be89-3c69c7ede75a/SRR16106002_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/68132dd2-6f0a-4373-8803-29c7543ef2d1?catalog=dcp28&version=2022-04-07T19%3A28%3A11.330000Z"
output="61807d1b-c7d0-4c56-be14-7d24ea2b9296/SRR16106094_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4aaa14bd-9de5-4d96-a4a2-87c4fac4189a?catalog=dcp28&version=2022-04-07T19%3A27%3A20.581000Z"
output="d0641426-1fc5-42ac-815f-604ddad42dfc/SRR16105873_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/28d74fac-4c5f-44e5-98e7-bbd166486e18?catalog=dcp28&version=2022-04-07T19%3A27%3A19.926000Z"
output="92c8a58a-35fe-4b44-96ab-f6305dd8eaab/SRR16105870_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/660eef84-f04d-4ee5-9ef4-a6845f51ed3a?catalog=dcp28&version=2022-04-07T19%3A26%3A56.399000Z"
output="9205f192-10b9-4044-be8b-ed22fac9c1dd/SRR16105764_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3b9edfd3-c010-4746-ad47-c1345194b975?catalog=dcp28&version=2022-04-07T19%3A26%3A57.718000Z"
output="83b293d7-fd54-461f-ae45-4f228d3b63fb/SRR16105791_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/92a16ae1-faaa-4cdd-98c2-f7bb90d51e59?catalog=dcp28&version=2022-04-07T19%3A26%3A59.420000Z"
output="ea20a490-8a70-46ed-aa47-df4cb27c25cd/SRR16105823_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c360bcff-89a9-4193-aa92-0fcdeeede307?catalog=dcp28&version=2022-04-07T19%3A27%3A56.829000Z"
output="9e497c89-2ba7-4422-8cdb-28a93eea8766/SRR16106015_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d1801821-e50e-4f6d-b3f0-bf8a3237ebf8?catalog=dcp28&version=2022-04-07T19%3A27%3A21.593000Z"
output="70a8b043-6ba0-499c-bcc5-37853b13d405/SRR16105881_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fc849d41-e685-4406-87eb-733ee6d38d86?catalog=dcp28&version=2022-04-07T19%3A27%3A17.944000Z"
output="398a6d0a-dd1f-4125-8508-8dbb0439b38e/SRR16105857_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/70f6919a-f54c-459e-b892-80e474425d9f?catalog=dcp28&version=2022-04-07T19%3A28%3A11.670000Z"
output="f5395a3a-99ca-426e-8e85-9264afd5b3e8/SRR16106098_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d2de5a86-6179-4bb5-b028-1e5b3f845500?catalog=dcp28&version=2022-04-07T19%3A26%3A57.474000Z"
output="c36bafbe-1e9d-46a6-9c6f-eedfb4a6f9be/SRR16105786_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e5f5912a-eedb-4423-b771-67a1c43db8d5?catalog=dcp28&version=2022-04-07T19%3A27%3A28.694000Z"
output="83f7466d-c72b-48d7-ad03-652e5a4ecb2e/SRR16105892_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3a33ad5a-4a2d-400d-a872-462c04d503d2?catalog=dcp28&version=2022-04-07T19%3A27%3A43.864000Z"
output="560607c8-3d51-4dd2-866f-4c09fb872727/SRR16105963_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b28ad6da-4399-4deb-981e-43a7891d3cb2?catalog=dcp28&version=2022-04-07T19%3A26%3A57.558000Z"
output="51d16b92-563a-40eb-9ceb-d7338bd7de8b/SRR16105788_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dd7e372b-29e2-4c7d-91bd-843e9a60209c?catalog=dcp28&version=2022-04-07T19%3A28%3A12.388000Z"
output="94316c6a-decf-400e-b9f1-9b2da2ee228c/SRR16106108_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6bc52c9f-8fb5-4d8a-b069-f4d7cb50d1b9?catalog=dcp28&version=2022-04-07T19%3A27%3A57.756000Z"
output="8200dd65-0c24-403c-b5b5-f01fc24092d3/SRR16106026_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/641a31db-d21c-4ed3-b8a2-d6edd746601f?catalog=dcp28&version=2022-04-07T19%3A28%3A09.832000Z"
output="77afdd55-5dc2-444f-b63e-e5bd7d9b9c44/SRR16106081_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e82fdb53-3fa6-4636-95b6-588fd660f8a5?catalog=dcp28&version=2022-04-07T19%3A27%3A05.797000Z"
output="49038b69-6ccd-4eff-bb48-988fc48c8038/SRR16105832_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d8772ae9-431d-4ab6-80a7-ad3d2e63a430?catalog=dcp28&version=2022-04-07T19%3A27%3A42.340000Z"
output="45a1481c-a462-4b18-9dd3-0bdf6ad981e0/SRR16105950_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f1a63d69-a3a1-4518-ad04-1dd5dc41222a?catalog=dcp28&version=2022-04-07T19%3A26%3A57.882000Z"
output="f4f1f564-781d-46a4-93b1-098c0b919e29/SRR16105793_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/681910f7-4661-40ae-96a6-421756725ab3?catalog=dcp28&version=2022-04-07T19%3A27%3A28.462000Z"
output="f386a906-d9cd-43cb-9020-b134a1bc466a/SRR16105891_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2168efe0-16f2-4eaf-aad9-be452df816a7?catalog=dcp28&version=2022-04-07T19%3A26%3A59.006000Z"
output="7c3bfac6-0cf9-444c-853b-668c48aa3f53/SRR16105816_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/005e091e-3fac-4cd2-a85c-c50238f6d02d?catalog=dcp28&version=2022-04-07T19%3A28%3A12.520000Z"
output="e3beebec-9471-4d19-b4b5-370fd4e6c427/SRR16106112_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cd83b8df-60d4-42f1-b552-5004691d46a9?catalog=dcp28&version=2022-04-07T19%3A27%3A57.328000Z"
output="cff878d8-8e62-4686-b73d-2feaf2813300/SRR16106020_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bcfd07b2-bfcc-4420-8bdc-304dd0aaaad6?catalog=dcp28&version=2022-04-07T19%3A27%3A42.926000Z"
output="8f54e440-8491-473d-a01b-5e47dc6b6210/SRR16105957_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e59d41c2-c7fc-425e-939a-f30dc029f0c3?catalog=dcp28&version=2022-04-07T19%3A27%3A27.730000Z"
output="3f2f7522-63af-46a0-b884-4d1c4092d0e9/SRR16105887_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2936dcb7-893b-484c-a883-c5ad54657d74?catalog=dcp28&version=2022-04-07T19%3A27%3A19.371000Z"
output="941885c8-4d6c-4824-bdc2-a61c29e1251e/SRR16105865_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fbc871e3-21bd-417a-874e-03a5ca795f84?catalog=dcp28&version=2022-04-07T19%3A26%3A56.387000Z"
output="971a0dd5-bb0d-49d9-b7f7-bfd4fc5fe4fc/SRR16105763_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bdf18793-2f34-4a44-acde-e86fd1a8431a?catalog=dcp28&version=2022-04-07T19%3A27%3A55.914000Z"
output="7787e4b9-1cbc-417c-b4e5-ce0f8ef76eb6/SRR16106007_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/00778fce-a27f-4898-84fa-e78d94694139?catalog=dcp28&version=2022-04-07T19%3A27%3A42.957000Z"
output="8f54e440-8491-473d-a01b-5e47dc6b6210/SRR16105957_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/339d9194-eded-47b7-9cd5-86b478d9f5b9?catalog=dcp28&version=2022-04-07T19%3A26%3A56.314000Z"
output="1a23c808-8cdd-48db-981a-1f5c2c12f8af/SRR16105762_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/32db91f4-1610-437d-892a-fa85ae574e38?catalog=dcp28&version=2022-04-07T19%3A27%3A47.976000Z"
output="00ab3054-0713-4559-a30a-52622d79bee4/SRR16105985_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dffbcc30-374a-4f49-95ec-a01c47ded297?catalog=dcp28&version=2022-04-07T19%3A28%3A00.982000Z"
output="2fdb0a8d-4d67-48f7-947b-e377f91e3d6a/SRR16106040_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fed5d225-fb0d-43d1-97a2-826463e119dd?catalog=dcp28&version=2022-04-07T19%3A28%3A09.877000Z"
output="77afdd55-5dc2-444f-b63e-e5bd7d9b9c44/SRR16106081_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fbe85bc6-b464-4b5d-bf3a-39b2862dd0b4?catalog=dcp28&version=2022-04-07T19%3A27%3A57.519000Z"
output="41fceb09-b7c8-40ce-b2d9-20eda5cbf63d/SRR16106023_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0541c3a4-6fbb-49a4-bf00-20277fb4e43a?catalog=dcp28&version=2022-04-07T19%3A27%3A46.774000Z"
output="0af2f0eb-bfd7-4de7-984a-1fa5b2f0236a/SRR16105984_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a7713821-f73b-4a58-a0bf-73a77e097c50?catalog=dcp28&version=2022-04-07T19%3A26%3A58.668000Z"
output="1136f513-4add-4317-ab09-61535c5ef07b/SRR16105809_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a57e0f21-d98b-41cc-b5bb-8b5e589a77ee?catalog=dcp28&version=2022-04-07T19%3A27%3A24.702000Z"
output="98eab227-ffd1-439e-b93a-68c6137da6e2/SRR16105883_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/95ecd8da-20fc-4673-9102-2652c2cc851e?catalog=dcp28&version=2022-04-07T19%3A27%3A54.547000Z"
output="9923f38c-329a-40d1-956d-d0dd9ac70a66/SRR16105998_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/27208ca7-95bf-4c34-b794-bc8d59e91a43?catalog=dcp28&version=2022-04-07T19%3A27%3A45.918000Z"
output="832587f4-4111-45b8-b134-5e66f5ee2da5/SRR16105981_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b5820f04-f3c0-42ec-992e-3f6b14e29b6a?catalog=dcp28&version=2022-04-07T19%3A28%3A11.224000Z"
output="de4f5178-3b57-4791-ac2a-786a4768480c/SRR16106092_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0227bcac-5149-4a41-ba0e-53998c402d48?catalog=dcp28&version=2022-04-07T19%3A27%3A58.171000Z"
output="afdc8ee8-c0e7-4fa0-b870-6daa37d5df9f/SRR16106031_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8b66e416-5aea-4e9d-9451-c7a0fabbe7d6?catalog=dcp28&version=2022-04-07T19%3A26%3A58.878000Z"
output="e74ab0d6-5b8f-4955-afbe-d56fd5d095b8/SRR16105814_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a1459b40-2c52-4361-8ea4-4a42352be220?catalog=dcp28&version=2022-04-07T19%3A27%3A43.099000Z"
output="d7f2c949-dffb-46cb-90e1-69506f812ddb/SRR16105959_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c82c5711-575b-467c-a719-4c6cadcc6529?catalog=dcp28&version=2022-04-07T19%3A26%3A58.908000Z"
output="ada83954-9c04-42b3-9bb9-9c0b23070fd6/SRR16105815_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1d7b70a7-772e-42f2-a93a-36e0fa13af66?catalog=dcp28&version=2022-04-07T19%3A27%3A45.862000Z"
output="76767309-75fa-48e7-82da-f8106341bfcd/SRR16105980_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/21f4afea-8f21-4af2-83d4-3567cd80d638?catalog=dcp28&version=2022-04-07T19%3A27%3A54.594000Z"
output="9923f38c-329a-40d1-956d-d0dd9ac70a66/SRR16105998_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c1616d15-769e-4102-8f89-daf3ac6a3640?catalog=dcp28&version=2022-04-07T19%3A26%3A56.034000Z"
output="d92fea69-f5b7-4609-9f51-54328b3e0e14/SRR16105755_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5e633cc1-171e-4bfe-958e-4ba1406bd304?catalog=dcp28&version=2022-04-07T19%3A27%3A49.967000Z"
output="514875d8-b2fc-4453-a4a9-ce2f052cdb78/SRR16105990_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/73931239-1cbd-48f3-81ee-96540a71c180?catalog=dcp28&version=2022-04-07T19%3A27%3A43.135000Z"
output="d7f2c949-dffb-46cb-90e1-69506f812ddb/SRR16105959_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/27f4efb0-ed3d-4015-96be-574d038533a6?catalog=dcp28&version=2022-04-07T19%3A27%3A30.307000Z"
output="ba60e59f-5da9-4f60-bd15-4186281ce060/SRR16105906_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a751ab31-e6d6-49f3-b9d9-7329238c3631?catalog=dcp28&version=2022-04-07T19%3A26%3A57.138000Z"
output="011d1060-e572-4124-b96e-cf3d8acd3016/SRR16105778_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ca221f35-2df2-4dfc-b6cc-6b1377dc972d?catalog=dcp28&version=2022-04-07T19%3A27%3A33.598000Z"
output="783fc31c-c3fd-44dc-9279-abf3c60b2dc8/SRR16105935_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0d3032c9-10d4-438f-8619-a714063f9bbe?catalog=dcp28&version=2022-04-07T19%3A27%3A43.076000Z"
output="3d2aebd8-a4e0-44fb-8037-b6a1a02fed9a/SRR16105958_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b635d6b3-bd6a-4590-8faa-6e07fdae9442?catalog=dcp28&version=2022-04-07T19%3A27%3A16.938000Z"
output="db5cb49d-1ce9-4ffc-b4fb-38b260573409/SRR16105849_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/640d3ff4-c5fd-4b14-900d-78cb746ed9c8?catalog=dcp28&version=2022-04-07T19%3A26%3A56.728000Z"
output="5d12fe38-12a4-4f00-af18-b902d081624b/SRR16105772_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3fd9bba5-31fe-436f-b4ba-e399e2cec6dd?catalog=dcp28&version=2022-04-07T19%3A26%3A56.286000Z"
output="e1128bb4-5805-47eb-ac5e-2cecf7f3dfa9/SRR16105761_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2debfd13-c547-4af5-a822-a5868e187e4a?catalog=dcp28&version=2022-04-07T19%3A27%3A44.591000Z"
output="a94914ce-d6c7-4a6b-a581-94b6287c6980/SRR16105971_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/018a097b-4dec-4261-8d90-f5a267b79e50?catalog=dcp28&version=2022-04-07T19%3A27%3A16.814000Z"
output="34898ed8-5e60-432c-b934-021842b4cfd8/SRR16105848_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a095cfb6-c459-47cd-a98a-2792f09e76b5?catalog=dcp28&version=2022-04-07T19%3A26%3A58.767000Z"
output="93d9a8f6-8813-4cfa-9c37-a1447f614a47/SRR16105811_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/11ad6eaf-44e8-4f9a-8d50-d8f492117427?catalog=dcp28&version=2022-04-07T19%3A27%3A30.033000Z"
output="c6e06e73-0d23-4764-95dc-b9952d6d9caf/SRR16105903_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bcbb362e-75d4-43ea-9021-590aa513b11b?catalog=dcp28&version=2022-04-07T19%3A27%3A55.955000Z"
output="7787e4b9-1cbc-417c-b4e5-ce0f8ef76eb6/SRR16106007_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/24e00acb-f712-4f2b-a098-f27ce882f050?catalog=dcp28&version=2022-04-07T19%3A28%3A09.796000Z"
output="de74d25d-e2c1-4c5e-9315-a13281938e7f/SRR16106080_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/be53d0b1-9b86-4250-b758-143dbd3e29bc?catalog=dcp28&version=2022-04-07T19%3A26%3A59.504000Z"
output="c7a45e4a-bc9c-49d9-85c9-98bfabe148b8/SRR16105824_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1d0a5500-c3de-411e-83b4-e52de9ae7120?catalog=dcp28&version=2022-04-07T19%3A27%3A39.572000Z"
output="759fef86-2f91-42e4-9122-f4ef6e3fdeac/SRR16105945_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0372c6a6-70b2-4b9f-a4e8-90747a207e71?catalog=dcp28&version=2022-04-07T19%3A27%3A21.560000Z"
output="70a8b043-6ba0-499c-bcc5-37853b13d405/SRR16105881_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fb04c3c7-f4ae-4003-8a5b-d28dbf53aa67?catalog=dcp28&version=2022-04-07T19%3A27%3A53.814000Z"
output="a133413a-01da-4f8d-84df-5896b14a73d5/SRR16105994_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d41bf399-c9b1-4c55-9cd8-09579cb923a8?catalog=dcp28&version=2022-04-07T19%3A27%3A41.972000Z"
output="37346a5a-99b2-465f-b0d4-1bba7616d547/SRR16105948_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/440f7bfc-23d6-4552-9095-39554f457133?catalog=dcp28&version=2022-04-07T19%3A28%3A08.070000Z"
output="aff1cdb9-840a-4f4b-8dbc-1a60620924da/SRR16106054_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/228ce97a-80c4-4441-9cf7-2a1b8d75f16b?catalog=dcp28&version=2022-04-07T19%3A27%3A58.076000Z"
output="724a9e10-bb44-4a94-8a50-2ff9636d46b0/SRR16106030_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e6ba2b1e-eddd-4a59-90ca-f6470b6749d8?catalog=dcp28&version=2022-04-07T19%3A26%3A59.685000Z"
output="6c902c8d-c727-4e3b-a2fa-fd8a09df9f31/SRR16105826_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6bf653ab-32c6-44d3-9604-90909db9dfbf?catalog=dcp28&version=2022-04-07T19%3A28%3A03.606000Z"
output="e703efca-f439-45e7-989a-51e9219896b4/SRR16106046_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/591c869b-17ac-4aa5-afd8-447a4c5ed097?catalog=dcp28&version=2022-04-07T19%3A26%3A59.318000Z"
output="92203ca9-480b-47c5-8f37-1137caa7a0f6/SRR16105822_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8fdf4f8f-20f3-4319-b544-bd6f00cff765?catalog=dcp28&version=2022-04-07T19%3A26%3A57.643000Z"
output="1dd51ef1-5ba1-4931-81da-9b82bec052dd/SRR16105790_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a5484048-71aa-4497-bba2-4312149ff9b9?catalog=dcp28&version=2022-04-07T19%3A26%3A56.906000Z"
output="fe2e00d7-e6ff-4f11-a376-da60874a7924/SRR16105776_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/aa1dabc8-30a1-448a-95a2-a2f73b0834d8?catalog=dcp28&version=2022-04-07T19%3A27%3A44.516000Z"
output="8f9ec997-f531-4f77-a32b-7e356a96daa5/SRR16105970_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2328ecb8-55a6-4248-a992-91e2efae1045?catalog=dcp28&version=2022-04-07T19%3A27%3A57.305000Z"
output="cff878d8-8e62-4686-b73d-2feaf2813300/SRR16106020_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e9e0288e-2975-43b2-8d89-b4344f0b296e?catalog=dcp28&version=2022-04-07T19%3A28%3A10.082000Z"
output="15e70126-0d04-40a3-b1bd-939bf7890b2f/SRR16106084_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ce515eb2-70da-431a-9424-55e796af5008?catalog=dcp28&version=2022-04-07T19%3A28%3A10.165000Z"
output="e206212b-035b-42d1-b0f2-b70f854f7f2b/SRR16106085_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/aaa09b17-e130-45fc-b893-32366bbc905b?catalog=dcp28&version=2022-04-07T19%3A27%3A58.196000Z"
output="afdc8ee8-c0e7-4fa0-b870-6daa37d5df9f/SRR16106031_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ac2cda63-1805-4895-83ad-4a04f98413d4?catalog=dcp28&version=2022-04-07T19%3A28%3A12.555000Z"
output="8a15abfd-b0db-4222-b59c-6032a0dced1a/SRR16106113_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/20c599f1-93c4-4d8b-85db-f2add0639548?catalog=dcp28&version=2022-04-07T19%3A27%3A13.998000Z"
output="aae5c048-65e4-4ca9-8d8e-e640a8eae9d4/SRR16105839_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/23e3d630-9425-4f22-a22f-ff444afe4562?catalog=dcp28&version=2022-04-07T19%3A26%3A58.626000Z"
output="1136f513-4add-4317-ab09-61535c5ef07b/SRR16105809_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f4d7aabf-db04-45a9-bc50-42ba56562ac2?catalog=dcp28&version=2022-04-07T19%3A28%3A11.887000Z"
output="e9b9cd07-16d8-442f-ba80-21afe8b98fad/SRR16106101_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/372da539-49cb-4031-957c-8fc203b473de?catalog=dcp28&version=2022-04-07T19%3A27%3A56.890000Z"
output="3ed57d69-7b79-4bff-8726-68caab01fecc/SRR16106016_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8f89bf17-4531-4715-9434-d61b5e7fc31f?catalog=dcp28&version=2022-04-07T19%3A27%3A31.711000Z"
output="20a8abe3-c25c-4736-a244-d66f6fd0ae91/SRR16105915_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a6f1fba3-f750-4cfe-833a-4e05a53eae20?catalog=dcp28&version=2022-04-07T19%3A27%3A57.899000Z"
output="da6cf693-ad4d-440a-a0e7-698653151e44/SRR16106028_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0f9b2a52-3223-44d0-86b8-c0292852dea2?catalog=dcp28&version=2022-04-07T19%3A28%3A11.258000Z"
output="de4f5178-3b57-4791-ac2a-786a4768480c/SRR16106092_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0e36b91f-3182-470c-b14f-91c5a0e1a877?catalog=dcp28&version=2022-04-07T19%3A27%3A44.403000Z"
output="bd3b5bfa-bb91-4a09-8737-67ac1da7af2f/SRR16105969_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/82d26894-aa31-4d37-bcf5-35c479ca99ad?catalog=dcp28&version=2022-04-07T19%3A27%3A58.361000Z"
output="753505f6-8367-4199-86fb-1e8a806a25a4/SRR16106033_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/35430c23-bbcb-479a-a8ec-717181f6fa4a?catalog=dcp28&version=2022-04-07T19%3A27%3A30.935000Z"
output="9d93665a-8355-41d3-bb89-e61678ad7437/SRR16105912_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5dcb3c2f-d15c-4923-a221-99bb7e014ea5?catalog=dcp28&version=2022-04-07T19%3A28%3A12.449000Z"
output="6197baee-5ca1-499c-a46f-2d3dee3ebe73/SRR16106110_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e6475f2b-405c-4b69-a1c2-2a789e11508a?catalog=dcp28&version=2022-04-07T19%3A28%3A09.645000Z"
output="35059cf0-2e3e-470d-9169-7b7cbe64e56a/SRR16106078_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3e758c63-b64c-4979-ba85-b04fbe0cd485?catalog=dcp28&version=2022-04-07T19%3A27%3A33.624000Z"
output="783fc31c-c3fd-44dc-9279-abf3c60b2dc8/SRR16105935_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c60ade6c-ede7-404c-94cf-364e4fe9dbff?catalog=dcp28&version=2022-04-07T19%3A27%3A42.203000Z"
output="a685b4b1-712e-4248-b180-ba4fff92e5d6/SRR16105949_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9a069dd9-2438-4f7a-b439-9a889df24964?catalog=dcp28&version=2022-04-07T19%3A27%3A46.149000Z"
output="636c619c-a2ec-4688-ba95-5990590fcc15/SRR16105983_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/daca84bd-7d3a-4963-ac6b-86ef0c0c2d0a?catalog=dcp28&version=2022-04-07T19%3A28%3A10.755000Z"
output="27dc5396-721a-4d2a-8115-09d986f6f605/SRR16106089_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8c6a2c0f-89b7-41eb-9193-40efcb372359?catalog=dcp28&version=2022-04-07T19%3A28%3A07.724000Z"
output="a2cb46e2-7db3-407c-bea9-05b68e01a059/SRR16106052_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/83480242-b93d-4ef1-8a08-5a1826627894?catalog=dcp28&version=2022-04-07T19%3A27%3A29.189000Z"
output="f13ff253-8785-47e8-805a-1a5a08ae8345/SRR16105895_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/56d42c73-05aa-4c32-a834-5889404bc94c?catalog=dcp28&version=2022-04-07T19%3A26%3A57.230000Z"
output="8df20e18-d035-4b7a-8e04-89a3522d2494/SRR16105781_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f5f0e54c-0293-4dcb-88a8-03e99531d443?catalog=dcp28&version=2022-04-07T19%3A27%3A35.449000Z"
output="38dedfdf-d9f5-4e8c-b49a-58960a26b9f0/SRR16105939_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/af601b14-2e72-4ea0-b8ae-6159e085745b?catalog=dcp28&version=2022-04-07T19%3A28%3A11.816000Z"
output="339fde68-d0a6-4e6d-bdca-9ef5cc084e34/SRR16106100_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6bb6755a-6b7c-4975-9a73-e9e105c112e4?catalog=dcp28&version=2022-04-07T19%3A27%3A42.807000Z"
output="f97d049e-dcbd-4d1a-9349-704cd1edd1fb/SRR16105955_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/db2eefd3-3146-4e13-80cd-2bf957d5e24b?catalog=dcp28&version=2022-04-07T19%3A27%3A32.606000Z"
output="3e6f7d88-6ab6-4dfd-b4f2-1371411780a7/SRR16105924_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cb40bfb1-88eb-47bc-aeb6-86f14964c4f1?catalog=dcp28&version=2022-04-07T19%3A28%3A01.264000Z"
output="cd69f208-db53-4efd-a474-035ce10620a4/SRR16106043_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e3f0e675-e3bc-4786-9d25-3382c7b9b24a?catalog=dcp28&version=2022-04-07T19%3A26%3A58.216000Z"
output="96fa2c80-1471-42e8-b163-5798b01dc749/SRR16105802_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3b38d810-a554-4c81-9017-6f02426b451c?catalog=dcp28&version=2022-04-07T19%3A27%3A16.707000Z"
output="75cb8029-0e19-47bb-a782-e9f4e89dfb09/SRR16105847_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/84c3fc06-af69-4b6f-999b-7ec5133bf625?catalog=dcp28&version=2022-04-07T19%3A28%3A08.899000Z"
output="ac70ba6e-eb5f-49b4-9dd3-c8c7987429f3/SRR16106069_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/18bc5a18-ae49-4f06-97d5-57145814419e?catalog=dcp28&version=2022-04-07T19%3A27%3A44.290000Z"
output="3f5de3bc-b858-401c-9d40-4aa744629a87/SRR16105968_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/02e9c2f9-329f-4bd1-a445-09c78273ae4f?catalog=dcp28&version=2022-04-07T19%3A26%3A56.172000Z"
output="d06b69d0-e91e-499c-8ce8-038faec09094/SRR16105758_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/daefee0b-158a-48e6-aa17-0115aed8ecf0?catalog=dcp28&version=2022-04-07T19%3A27%3A21.201000Z"
output="685db304-d1d0-4263-806e-f1051093a1db/SRR16105878_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4584bf26-1930-4bf5-9c2e-1c5ecb5cf0a0?catalog=dcp28&version=2022-04-07T19%3A27%3A48.664000Z"
output="0443a18a-5a33-4c34-aa6e-3d6fb4c16a05/SRR16105986_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7b21d633-51f4-4f86-b46d-c4029846eb52?catalog=dcp28&version=2022-04-07T19%3A27%3A15.124000Z"
output="aae5c048-65e4-4ca9-8d8e-e640a8eae9d4/SRR16105839_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9e7978e7-d84a-4658-91cd-91cd9c616d13?catalog=dcp28&version=2022-04-07T19%3A26%3A59.395000Z"
output="ea20a490-8a70-46ed-aa47-df4cb27c25cd/SRR16105823_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/88eeed2a-2b96-4895-9df8-a9c6e2cdae80?catalog=dcp28&version=2022-04-07T19%3A26%3A58.168000Z"
output="8f5e7b77-9b95-4f02-b39b-6fd721cd2de0/SRR16105800_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a30b5a9b-35a3-4d11-a784-f259931b36fa?catalog=dcp28&version=2022-04-07T19%3A28%3A12.311000Z"
output="56842abf-71b1-4f34-9655-65587315944c/SRR16106106_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1826bb31-2787-4c15-9cfd-0e70b1d6d1d4?catalog=dcp28&version=2022-04-07T19%3A27%3A44.893000Z"
output="f575dc89-29eb-4c14-9951-03903f35551f/SRR16105973_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/02b3cff9-67bd-4cfa-b583-aac713e7fd03?catalog=dcp28&version=2022-04-07T19%3A27%3A27.385000Z"
output="fb0e10ac-3443-4fad-a6fd-53dd612610a7/SRR16105885_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/31db57b7-88ab-4505-b580-4aa543cb0b45?catalog=dcp28&version=2022-04-07T19%3A28%3A08.370000Z"
output="9029d12d-3d92-48e9-a135-a184dc5f7746/SRR16106058_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ae6928a7-b2d7-4297-a556-8c415cf4e122?catalog=dcp28&version=2022-04-07T19%3A27%3A03.280000Z"
output="339859d9-009d-4f94-9a39-5e1e79108ec8/SRR16105831_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/39ed7a09-0d5c-44c7-92d4-503c1e02a261?catalog=dcp28&version=2022-04-07T19%3A27%3A32.212000Z"
output="16ecac57-9888-4133-8853-a2daf5aaf528/SRR16105921_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2f9197ab-04d3-41f0-b8a3-8a4445cd782b?catalog=dcp28&version=2022-04-07T19%3A28%3A08.405000Z"
output="9029d12d-3d92-48e9-a135-a184dc5f7746/SRR16106058_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2c4eac59-19f8-479e-85e9-0ebae1937a34?catalog=dcp28&version=2022-04-07T19%3A27%3A16.441000Z"
output="0d27c127-1fea-4f7b-b54e-4a7a06d8b1cc/SRR16105844_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/950bdece-cea4-4df1-a853-0c3a9809c60b?catalog=dcp28&version=2022-04-07T19%3A28%3A01.422000Z"
output="3fa51f19-f8ff-46e7-8843-adc53f852b11/SRR16106044_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/75596d21-bcc8-405d-99e6-3fb3a5f6ad8e?catalog=dcp28&version=2022-04-07T19%3A27%3A16.553000Z"
output="43acafb6-087d-4d7f-bf32-643c83723170/SRR16105846_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a8e06492-b027-47df-8529-6d60cf4feaab?catalog=dcp28&version=2022-04-07T19%3A27%3A46.242000Z"
output="636c619c-a2ec-4688-ba95-5990590fcc15/SRR16105983_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cce4f1d2-ca69-4013-9c3f-b7a691375e88?catalog=dcp28&version=2022-04-07T19%3A28%3A07.478000Z"
output="db2ac85a-6c6c-4f1b-a7bc-8eaf8b1fd124/SRR16106050_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4254c939-57f0-4751-8596-2aa9a8b667f7?catalog=dcp28&version=2022-04-07T19%3A27%3A29.661000Z"
output="81817ea5-b474-4514-b789-e593e7211b16/SRR16105899_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d9f8af70-aa1d-4181-9293-2eecb6fea897?catalog=dcp28&version=2022-04-07T19%3A28%3A02.487000Z"
output="d6ecb457-a871-41d5-b2de-92ba4fadf9ae/SRR16106045_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9863278a-daff-4b21-9197-86f44fb355da?catalog=dcp28&version=2022-04-07T19%3A26%3A58.795000Z"
output="23ef0a1d-b646-4c01-8959-f8af1070e46f/SRR16105812_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/47b2961b-7a11-427d-b6b7-ca54fcd5e6ce?catalog=dcp28&version=2022-04-07T19%3A27%3A45.946000Z"
output="832587f4-4111-45b8-b134-5e66f5ee2da5/SRR16105981_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/99136c06-ac57-4dc8-b925-9395da09547b?catalog=dcp28&version=2022-04-07T19%3A28%3A08.046000Z"
output="aff1cdb9-840a-4f4b-8dbc-1a60620924da/SRR16106054_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0f9162d5-ea1f-4e3d-9706-c1a74d378c47?catalog=dcp28&version=2022-04-07T19%3A27%3A54.066000Z"
output="84d493d1-968f-4520-892d-3331d900b8f9/SRR16105995_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e7353cc6-fca8-4bbc-9101-331e8b575f53?catalog=dcp28&version=2022-04-07T19%3A28%3A11.719000Z"
output="23b42a69-274c-41f6-acd4-a466732254ac/SRR16106099_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/72ced66a-332a-438a-a66e-2bd1c0e32079?catalog=dcp28&version=2022-04-07T19%3A28%3A12.461000Z"
output="6197baee-5ca1-499c-a46f-2d3dee3ebe73/SRR16106110_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b7eeff39-be46-4381-b3ce-c0e942f6a8e2?catalog=dcp28&version=2022-04-07T19%3A26%3A56.274000Z"
output="e1128bb4-5805-47eb-ac5e-2cecf7f3dfa9/SRR16105761_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bb7ae64e-8d8b-48eb-b51d-65ac536ac0b7?catalog=dcp28&version=2022-04-07T19%3A27%3A18.389000Z"
output="a256c6e1-278c-43cd-a863-818f1f6866da/SRR16105861_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2828a8f9-dcbe-414d-b866-edfb4e782c51?catalog=dcp28&version=2022-04-07T19%3A28%3A00.798000Z"
output="bd3f8f43-09c9-4df0-8ce5-0f57f98f1c3a/SRR16106038_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6fa17329-a997-48da-966e-997d8998a937?catalog=dcp28&version=2022-04-07T19%3A28%3A08.943000Z"
output="66ceee2f-7c84-458d-b713-bf74a8a93de7/SRR16106070_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2872455a-af33-492b-890f-a8d881bf6908?catalog=dcp28&version=2022-04-07T19%3A26%3A59.476000Z"
output="c7a45e4a-bc9c-49d9-85c9-98bfabe148b8/SRR16105824_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4ce0a220-f107-4bc4-bbc0-9e101d97a975?catalog=dcp28&version=2022-04-07T19%3A26%3A57.685000Z"
output="83b293d7-fd54-461f-ae45-4f228d3b63fb/SRR16105791_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6d03a4c1-c145-49af-b81b-da7a082f6ee9?catalog=dcp28&version=2022-04-07T19%3A27%3A27.694000Z"
output="3f2f7522-63af-46a0-b884-4d1c4092d0e9/SRR16105887_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/11989704-a190-4dde-b13f-471f670ecb8d?catalog=dcp28&version=2022-04-07T19%3A27%3A55.183000Z"
output="f2c687f8-b12c-46a2-815b-08329f279144/SRR16106003_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c60c928c-d8cd-4c72-9335-0b691f412d14?catalog=dcp28&version=2022-04-07T19%3A26%3A56.641000Z"
output="a678f0bd-c71d-4557-a524-90f6f0ec7f78/SRR16105770_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e8ec2b00-8c6c-4dd6-85c1-eca970636acb?catalog=dcp28&version=2022-04-07T19%3A27%3A18.091000Z"
output="c89e1023-7a12-4f75-b097-617ae9cf0a4e/SRR16105858_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1a85eb54-9bc9-4c81-8b75-80f10f788f11?catalog=dcp28&version=2022-04-07T19%3A27%3A27.524000Z"
output="8f6dec87-e785-4575-b8d6-e6418f5c7133/SRR16105886_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/44571896-9566-43b2-9bea-4d2660e82c64?catalog=dcp28&version=2022-04-07T19%3A27%3A30.556000Z"
output="5fdc2a0f-c761-48fc-9204-402011d61a06/SRR16105908_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a2437ae8-3019-4468-8f9b-09a75c4f6c6b?catalog=dcp28&version=2022-04-07T19%3A26%3A57.906000Z"
output="5973faea-848d-407a-a249-85ba85264249/SRR16105794_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dc1d6338-0162-488a-8495-267e5f6ef0c6?catalog=dcp28&version=2022-04-07T19%3A27%3A21.317000Z"
output="750ee074-c01f-4378-bea9-53e746bf1b07/SRR16105879_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4f3a8a96-49b2-49f0-b72b-b9e756c4ceb6?catalog=dcp28&version=2022-04-07T19%3A27%3A43.969000Z"
output="1e4f8657-7fd1-446e-a0ac-0fe3c567b6be/SRR16105964_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/064c468c-d832-498e-b071-b168d47a16a8?catalog=dcp28&version=2022-04-07T19%3A27%3A40.894000Z"
output="c71a8645-5e08-44c1-829c-b03d26855b48/SRR16105946_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2a6d65e5-2de0-4298-ab03-6e35d3bdd5d4?catalog=dcp28&version=2022-04-07T19%3A27%3A55.665000Z"
output="608f4800-5e5f-4358-9043-c6bcd2b34562/SRR16106005_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/67a0118c-8884-45dd-8aea-4b0f13d2c85a?catalog=dcp28&version=2022-04-07T19%3A26%3A56.159000Z"
output="d06b69d0-e91e-499c-8ce8-038faec09094/SRR16105758_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4f2c199b-8d77-4dd7-8579-31682696e317?catalog=dcp28&version=2022-04-07T19%3A27%3A36.327000Z"
output="16b37a5b-1e60-41e4-9c89-3a9cf352cd34/SRR16105941_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0feb1d7d-1748-4e77-94b9-566a8393671f?catalog=dcp28&version=2022-04-07T19%3A27%3A16.534000Z"
output="58c697f6-f768-4945-a107-055de56fe6b2/SRR16105845_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a0897161-ab3d-4a50-b87a-84e59260d483?catalog=dcp28&version=2022-04-07T19%3A27%3A19.520000Z"
output="7cae2684-20ec-4295-9010-46d6ab358dee/SRR16105867_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f262b56e-b4ae-47fd-8674-444d8e5349b9?catalog=dcp28&version=2022-04-07T19%3A28%3A00.536000Z"
output="f28f7f6f-87b3-48ca-b441-b24447ef1f58/SRR16106036_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a3836034-4bf2-408c-84a7-8c437790fc74?catalog=dcp28&version=2022-04-07T19%3A28%3A01.088000Z"
output="9781bbc9-74e7-4d79-94d6-0d46774211eb/SRR16106041_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e1018df5-3b92-44ae-91a5-24186cd661a0?catalog=dcp28&version=2022-04-07T19%3A28%3A12.401000Z"
output="714f1455-b491-4644-be6a-31331c89e459/SRR16106109_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/449998d7-c187-4876-bec2-64a4ccfb1ffc?catalog=dcp28&version=2022-04-07T19%3A28%3A11.606000Z"
output="cc0a9e54-c45e-4065-a662-fdeb71001fc6/SRR16106097_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5be8153e-4908-471d-bcea-8c1a612614c5?catalog=dcp28&version=2022-04-07T19%3A27%3A30.662000Z"
output="efb14c76-39db-469e-857f-4785a686f671/SRR16105909_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9859f3dc-c00a-492b-a698-5136350bc3f3?catalog=dcp28&version=2022-04-07T19%3A27%3A32.462000Z"
output="06fb0d09-a800-40b6-838d-1c20d78ecbdc/SRR16105923_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1fa64359-04de-4e7d-84db-5c5b0b0bc546?catalog=dcp28&version=2022-04-07T19%3A26%3A58.822000Z"
output="a6c579bc-a1fd-4e2f-8848-d7fa40ecada9/SRR16105813_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2ec1237d-8fcd-4baa-9b5f-0eb506e55e36?catalog=dcp28&version=2022-04-07T19%3A26%3A57.108000Z"
output="011d1060-e572-4124-b96e-cf3d8acd3016/SRR16105778_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0a6b3151-a835-45f4-b46f-d99803c39e7b?catalog=dcp28&version=2022-04-07T19%3A27%3A52.282000Z"
output="16e9ea04-bc15-4d39-8bce-5ab6c3d1a773/SRR16105992_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0911a5c0-3f47-4d84-ab3c-3fa1f8eede65?catalog=dcp28&version=2022-04-07T19%3A28%3A10.580000Z"
output="723d3641-f105-4d87-9657-af3ae9e6032e/SRR16106088_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a9819349-7aa4-4212-9184-628653558e1b?catalog=dcp28&version=2022-04-07T19%3A27%3A29.490000Z"
output="1b25e304-4e6a-479c-bf73-cb5254b6e7db/SRR16105898_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cdcabc80-b73d-45f6-8f77-66f8483c5d06?catalog=dcp28&version=2022-04-07T19%3A26%3A58.192000Z"
output="5d12037a-0a50-421c-84e0-367c12f41b55/SRR16105801_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fe0168ba-0329-4e2f-b7b4-2d330706ac38?catalog=dcp28&version=2022-04-07T19%3A27%3A54.449000Z"
output="f3303ed5-9cd3-4349-931d-3767f2f0eba0/SRR16105997_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1f32c0f3-1e7a-4f2c-b56f-6f79eab5d543?catalog=dcp28&version=2022-04-07T19%3A28%3A10.257000Z"
output="8ad0eecd-61c4-4eb3-8201-6d72def553d6/SRR16106086_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fc2d64ee-46f1-4689-accc-646d22be681f?catalog=dcp28&version=2022-04-07T19%3A28%3A07.530000Z"
output="d37506f9-06bc-4bb8-b71e-991af1edca45/SRR16106051_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f92f7014-7466-4849-909f-7df256c3079e?catalog=dcp28&version=2022-04-07T19%3A28%3A07.772000Z"
output="a2cb46e2-7db3-407c-bea9-05b68e01a059/SRR16106052_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4a439ce2-704a-4000-afb4-98306ae83720?catalog=dcp28&version=2022-04-07T19%3A26%3A59.285000Z"
output="eb093031-aedd-4fa6-a5cc-b380e928ac34/SRR16105821_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cf5560a1-7ccf-4be2-9e6d-8e980e15566e?catalog=dcp28&version=2022-04-07T19%3A27%3A54.425000Z"
output="a50015b5-0ec1-4950-acf2-be9b5873b98e/SRR16105996_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f9dc27c5-13f0-4963-be62-580753e91a00?catalog=dcp28&version=2022-04-07T19%3A28%3A07.887000Z"
output="a2cb46e2-7db3-407c-bea9-05b68e01a059/SRR16106052_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/682c6c8d-5953-41e0-b99c-0681b3b76381?catalog=dcp28&version=2022-04-07T19%3A28%3A10.287000Z"
output="8396361d-c7d1-4f3d-ae60-b9b1da6a76ce/SRR16106087_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1828b6e3-d573-4d7a-8033-51ea90536c1f?catalog=dcp28&version=2022-04-07T19%3A26%3A58.727000Z"
output="9b8aca24-d1fe-4c91-b144-98225db0ac0b/SRR16105810_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4af0b747-6356-4129-9e49-3d3d9622106b?catalog=dcp28&version=2022-04-07T19%3A26%3A57.427000Z"
output="1cc5a3bc-db79-481b-9a57-8f0683c3ae1a/SRR16105785_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/55497b25-452f-4d50-a966-1d1da6b4bbdb?catalog=dcp28&version=2022-04-07T19%3A28%3A11.920000Z"
output="e9b9cd07-16d8-442f-ba80-21afe8b98fad/SRR16106101_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/64df70e2-4cf5-4c0c-a1d7-bb16f95fff54?catalog=dcp28&version=2022-04-07T19%3A27%3A58.342000Z"
output="753505f6-8367-4199-86fb-1e8a806a25a4/SRR16106033_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/97aae733-b8d3-4fce-8c3d-e07eac23c3b9?catalog=dcp28&version=2022-04-07T19%3A27%3A18.447000Z"
output="a256c6e1-278c-43cd-a863-818f1f6866da/SRR16105861_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7e28719b-9970-4971-8575-213b76b48e4e?catalog=dcp28&version=2022-04-07T19%3A27%3A22.985000Z"
output="046a1865-03a8-4dcd-a6cc-795e98a42add/SRR16105882_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/619d2a44-920d-4e46-a89e-62f6297ea8ad?catalog=dcp28&version=2022-04-07T19%3A27%3A28.078000Z"
output="c9ee4eac-15d3-410a-8ba8-8926fe8d4fcb/SRR16105889_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b99d47af-a984-4f96-beba-f7ea6c300adb?catalog=dcp28&version=2022-04-07T19%3A27%3A13.298000Z"
output="b6ff1eea-cb66-412d-94ce-57a04e83b50e/SRR16105838_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/70666dcb-d229-4ba6-ae59-76e8c10f82d7?catalog=dcp28&version=2022-04-07T19%3A26%3A56.801000Z"
output="25d1cb64-8f8a-4593-a647-9a12bf33ca81/SRR16105774_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b0fd7d9f-6ba5-419a-b865-0cddb3b63876?catalog=dcp28&version=2022-04-07T19%3A26%3A56.222000Z"
output="1371b4ed-f5af-49bb-a96e-1ccfca16cad0/SRR16105760_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bdeda2b3-4fec-4f0e-a003-07790e2c7b0e?catalog=dcp28&version=2022-04-07T19%3A27%3A32.294000Z"
output="16ecac57-9888-4133-8853-a2daf5aaf528/SRR16105921_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/44fc7c88-8446-4d48-981e-a6171f12dd30?catalog=dcp28&version=2022-04-07T19%3A26%3A58.240000Z"
output="96fa2c80-1471-42e8-b163-5798b01dc749/SRR16105802_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/39ac98e3-7022-4f34-a0ff-0b2ceae92818?catalog=dcp28&version=2022-04-07T19%3A27%3A33.318000Z"
output="9a1699a3-b337-452b-8a88-b47b3d9cc44f/SRR16105932_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d194f618-4c6d-491a-9e82-9eb3326c1ab7?catalog=dcp28&version=2022-04-07T19%3A27%3A13.610000Z"
output="b6ff1eea-cb66-412d-94ce-57a04e83b50e/SRR16105838_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fc0736b7-f9d8-45c5-bae3-31c388cbc1d6?catalog=dcp28&version=2022-04-07T19%3A28%3A10.385000Z"
output="8396361d-c7d1-4f3d-ae60-b9b1da6a76ce/SRR16106087_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/417361c7-8139-4d71-bc6a-af12f051484c?catalog=dcp28&version=2022-04-07T19%3A27%3A58.749000Z"
output="aee6026d-07c1-47f7-b443-b31d4ddf4e26/SRR16106034_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5d3b3a3f-b2eb-4a74-b3f6-7c83844210ee?catalog=dcp28&version=2022-04-07T19%3A27%3A44.566000Z"
output="a94914ce-d6c7-4a6b-a581-94b6287c6980/SRR16105971_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4d3b7ee2-f36c-453a-bdc9-3ab4a65d126d?catalog=dcp28&version=2022-04-07T19%3A27%3A31.981000Z"
output="0386a58f-f2a9-4a8d-b0a5-1f5e954bcbd7/SRR16105918_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a4036bca-f267-460f-a6c9-ee076553b923?catalog=dcp28&version=2022-04-07T19%3A26%3A56.329000Z"
output="1a23c808-8cdd-48db-981a-1f5c2c12f8af/SRR16105762_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/83295cbf-361c-4ee2-bc23-e7fde1f1c5d7?catalog=dcp28&version=2022-04-07T19%3A27%3A37.137000Z"
output="16b37a5b-1e60-41e4-9c89-3a9cf352cd34/SRR16105941_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/171bef50-196f-4303-bcd1-ee0e9200f00f?catalog=dcp28&version=2022-04-07T19%3A27%3A58.094000Z"
output="724a9e10-bb44-4a94-8a50-2ff9636d46b0/SRR16106030_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/37b30a2f-aaa3-4879-b7c6-df0dad1cf81a?catalog=dcp28&version=2022-04-07T19%3A27%3A15.526000Z"
output="aae5c048-65e4-4ca9-8d8e-e640a8eae9d4/SRR16105839_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3431ea33-1adc-474e-a797-cce4a1b7482f?catalog=dcp28&version=2022-04-07T19%3A27%3A27.896000Z"
output="c9ee4eac-15d3-410a-8ba8-8926fe8d4fcb/SRR16105889_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cffe791c-edb7-4fd6-96a6-3687ecb9e48c?catalog=dcp28&version=2022-04-07T19%3A28%3A12.273000Z"
output="44ffb286-e933-45fd-97bb-ed3ff996cd9d/SRR16106105_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/deb89db0-4473-4f93-8c4b-58ba2127b7d2?catalog=dcp28&version=2022-04-07T19%3A26%3A56.552000Z"
output="31806f69-282e-40a1-9204-98ab7bd60d0f/SRR16105768_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/217c34c1-bb37-4fdc-a6b3-87bcd720dbea?catalog=dcp28&version=2022-04-07T19%3A28%3A10.966000Z"
output="d931e4f2-33e9-4233-9502-1dfd77a21d8c/SRR16106090_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2fdcf849-113b-47f9-9b57-31693c27b1a0?catalog=dcp28&version=2022-04-07T19%3A27%3A20.898000Z"
output="6d41648e-e6bb-4b77-924f-beae862055d0/SRR16105875_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/25e2ee41-45c4-4568-9ca3-1eec305544eb?catalog=dcp28&version=2022-04-07T19%3A28%3A09.810000Z"
output="de74d25d-e2c1-4c5e-9315-a13281938e7f/SRR16106080_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e40538b9-6f3e-4964-a67c-0d38154459be?catalog=dcp28&version=2022-04-07T19%3A27%3A33.758000Z"
output="03c7c566-9588-4697-a78c-75e85d70e3e5/SRR16105936_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/adc47c6f-cdf0-4953-a64e-d2dd4349cd6b?catalog=dcp28&version=2022-04-07T19%3A27%3A58.264000Z"
output="44681fe6-eb3e-4509-bc14-efc39eb0ee06/SRR16106032_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/43680b9d-725f-478f-b27e-be8dc2dd87c6?catalog=dcp28&version=2022-04-07T19%3A27%3A33.371000Z"
output="9a1699a3-b337-452b-8a88-b47b3d9cc44f/SRR16105932_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1bb07a59-e77d-4eca-877b-22102c3d3c6d?catalog=dcp28&version=2022-04-07T19%3A27%3A50.316000Z"
output="c5806b47-3a16-4319-baa2-dc014e981cb8/SRR16105991_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2ddc5733-3702-4e19-b6c1-e933434ae689?catalog=dcp28&version=2022-04-07T19%3A27%3A21.273000Z"
output="685db304-d1d0-4263-806e-f1051093a1db/SRR16105878_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e3241be4-e1de-4306-837f-a5cca02a8a64?catalog=dcp28&version=2022-04-07T19%3A28%3A00.321000Z"
output="cf3ffb3a-7ea2-4266-b4db-5fa6c850e5b2/SRR16106035_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2ec36746-eb13-4636-95bd-6726ab328d42?catalog=dcp28&version=2022-04-07T19%3A27%3A08.190000Z"
output="cd97de50-ba1b-42e3-ae2f-8e34a90eb766/SRR16105835_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d9308b71-2c98-4834-9d64-f668ef487334?catalog=dcp28&version=2022-04-07T19%3A27%3A37.526000Z"
output="d49f7948-f3c6-4fcd-8552-43d0e4ade6c1/SRR16105943_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/18b0a099-824b-4d62-8f7d-2da9afc4295c?catalog=dcp28&version=2022-04-07T19%3A27%3A57.394000Z"
output="8de871f4-4a62-4667-b5a0-59e8648d9a10/SRR16106021_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0639d1ca-0bfd-40b0-8530-e03df2f9124b?catalog=dcp28&version=2022-04-07T19%3A27%3A33.572000Z"
output="6c955fe5-cfc0-425c-942b-8f2ccd4139c5/SRR16105934_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3516a494-b896-49e1-8cd8-f25a99b806ce?catalog=dcp28&version=2022-04-07T19%3A28%3A11.110000Z"
output="94662222-bc39-4187-870e-a1d467c95b98/SRR16106091_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ba75562d-b207-4901-ad7c-b7f0678e6d26?catalog=dcp28&version=2022-04-07T19%3A27%3A28.539000Z"
output="f386a906-d9cd-43cb-9020-b134a1bc466a/SRR16105891_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e5b5b497-3544-4d72-97dc-367f6b0662e7?catalog=dcp28&version=2022-04-07T19%3A28%3A12.640000Z"
output="7e3af873-a224-4f4f-8b19-85093eafe0fc/SRR16106115_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/38e9eea7-d630-4894-b80d-baf8a7f1073a?catalog=dcp28&version=2022-04-07T19%3A27%3A28.735000Z"
output="7f951a6e-5541-45d8-bca2-ca3477480664/SRR16105893_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c2d479d3-e445-4e7a-afea-de944c02f4c0?catalog=dcp28&version=2022-04-07T19%3A27%3A27.660000Z"
output="3f2f7522-63af-46a0-b884-4d1c4092d0e9/SRR16105887_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b7267a1a-aa9a-454a-a521-4fcc3e649c12?catalog=dcp28&version=2022-04-07T19%3A26%3A57.254000Z"
output="8df20e18-d035-4b7a-8e04-89a3522d2494/SRR16105781_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/427d3819-d0a0-426c-aa6e-d264ae8c6834?catalog=dcp28&version=2022-04-07T19%3A27%3A17.219000Z"
output="74dbd63a-80a5-4cfd-b9d5-05a637ffc901/SRR16105851_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3b879c63-2abc-455a-bdbe-f699e4357bf3?catalog=dcp28&version=2022-04-07T19%3A27%3A04.322000Z"
output="49038b69-6ccd-4eff-bb48-988fc48c8038/SRR16105832_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b30d60b1-9b3c-4326-9c1f-4a23c53db411?catalog=dcp28&version=2022-04-07T19%3A27%3A42.281000Z"
output="a685b4b1-712e-4248-b180-ba4fff92e5d6/SRR16105949_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2930a3a8-b100-4fd1-8c40-88d168d7875f?catalog=dcp28&version=2022-04-07T19%3A26%3A56.098000Z"
output="b02a047d-33bf-4a58-b920-2a296516f007/SRR16105756_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b0275a49-ccbe-4725-9bd0-aef9921e0f17?catalog=dcp28&version=2022-04-07T19%3A27%3A38.645000Z"
output="14972570-4961-433f-8ad2-a08faf27941f/SRR16105944_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1f27c6ab-4990-4e32-8389-6070e06a8175?catalog=dcp28&version=2022-04-07T19%3A27%3A45.623000Z"
output="ac214f2f-64cb-45be-bcd8-1957b48ea0c8/SRR16105978_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f000b392-febe-4aa1-946e-c9237c2ff4cc?catalog=dcp28&version=2022-04-07T19%3A27%3A48.928000Z"
output="d1ad8f6f-5d92-486f-85bf-e8cdba503351/SRR16105988_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e57d7a31-2a35-45df-992e-f73b80870b3d?catalog=dcp28&version=2022-04-07T19%3A27%3A55.125000Z"
output="f2c687f8-b12c-46a2-815b-08329f279144/SRR16106003_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d8bb9ff1-5833-43b2-a6c9-c07c60c4e5de?catalog=dcp28&version=2022-04-07T19%3A26%3A58.278000Z"
output="51699d38-4e97-49a0-aa75-fa27901b3f02/SRR16105803_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/299e4f02-1035-4646-bea6-38e178e8e1de?catalog=dcp28&version=2022-04-07T19%3A27%3A29.376000Z"
output="fa0de6b6-c530-4a21-b41d-ca8c94299717/SRR16105896_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c61bc554-45bf-495c-b364-5abc4411234c?catalog=dcp28&version=2022-04-07T19%3A27%3A40.009000Z"
output="759fef86-2f91-42e4-9122-f4ef6e3fdeac/SRR16105945_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b92b5d31-f206-49b1-a7fd-f4cf697ff1cd?catalog=dcp28&version=2022-04-07T19%3A26%3A57.289000Z"
output="4f083e47-dc2d-4984-9f39-dbc062aa6ba5/SRR16105782_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0043cbd9-20c6-4b50-8c04-1e3ebf9ebc2f?catalog=dcp28&version=2022-04-07T19%3A27%3A16.893000Z"
output="db5cb49d-1ce9-4ffc-b4fb-38b260573409/SRR16105849_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/86862f9a-323a-4361-9604-aae755e09830?catalog=dcp28&version=2022-04-07T19%3A27%3A07.678000Z"
output="ce6d1e9b-d8d7-4a65-9f0f-869665816f2d/SRR16105834_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/33a12fe1-b031-4f80-8770-824afd9e6793?catalog=dcp28&version=2022-04-07T19%3A27%3A46.046000Z"
output="167ab68e-567a-410e-bcf0-88519336d72c/SRR16105982_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bf79f4aa-5331-42a8-b1f8-a4ea0e9d96c1?catalog=dcp28&version=2022-04-07T19%3A28%3A11.530000Z"
output="c7c1d756-e4e9-4857-8c24-ba4eaafe9507/SRR16106096_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1bd49e0a-e6c7-4ba1-9091-5a6db47ac735?catalog=dcp28&version=2022-04-07T19%3A27%3A30.728000Z"
output="ac5c9c01-3124-42a5-8191-c76c8f5ee22b/SRR16105910_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/daea26ad-1576-4607-b334-937764315cf8?catalog=dcp28&version=2022-04-07T19%3A26%3A58.315000Z"
output="34a12e21-0d7d-40e5-9e02-2e303ee76eed/SRR16105804_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c3814dc6-b6d1-4e0d-9ebc-3ae9c7739bed?catalog=dcp28&version=2022-04-07T19%3A27%3A18.067000Z"
output="c89e1023-7a12-4f75-b097-617ae9cf0a4e/SRR16105858_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d320dbb4-84ad-48a4-a8dc-eccb0ffa33b5?catalog=dcp28&version=2022-04-07T19%3A28%3A09.346000Z"
output="20efe407-47b3-4323-834f-33088f530e9f/SRR16106073_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ca17c9cf-7683-4754-8d5c-63676007e108?catalog=dcp28&version=2022-04-07T19%3A27%3A42.168000Z"
output="37346a5a-99b2-465f-b0d4-1bba7616d547/SRR16105948_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7a6faf64-4315-4e6d-85d3-2be3bbc3e523?catalog=dcp28&version=2022-04-07T19%3A27%3A21.181000Z"
output="b1942f46-14bb-445b-a046-de970f4924e7/SRR16105877_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8d83cc9f-7c90-4a96-938c-82a44d215cf1?catalog=dcp28&version=2022-04-07T19%3A27%3A44.351000Z"
output="3f5de3bc-b858-401c-9d40-4aa744629a87/SRR16105968_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/92262997-0605-4168-b7e8-47f2560eab91?catalog=dcp28&version=2022-04-07T19%3A27%3A32.004000Z"
output="1dc08504-d51f-4e75-be9d-90d9ee5c76ac/SRR16105919_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2b4545dc-198f-40db-bcaf-304bfed78ca1?catalog=dcp28&version=2022-04-07T19%3A27%3A29.732000Z"
output="e024c21f-2e54-45cf-9212-bcb34de475cb/SRR16105900_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/69cf44bc-60ad-4fd7-816b-a8d1cc26a2fa?catalog=dcp28&version=2022-04-07T19%3A28%3A11.856000Z"
output="339fde68-d0a6-4e6d-bdca-9ef5cc084e34/SRR16106100_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7c459470-949c-46de-bf8b-a2a054cafda7?catalog=dcp28&version=2022-04-07T19%3A26%3A56.261000Z"
output="e1128bb4-5805-47eb-ac5e-2cecf7f3dfa9/SRR16105761_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/309155f2-ddb6-420b-b93b-06b47679c033?catalog=dcp28&version=2022-04-07T19%3A27%3A49.110000Z"
output="0c3336b3-d21e-459c-a1d8-cb792a141631/SRR16105989_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6d17d07b-cdb5-495e-8e0e-dadfb39ff66f?catalog=dcp28&version=2022-04-07T19%3A26%3A58.266000Z"
output="51699d38-4e97-49a0-aa75-fa27901b3f02/SRR16105803_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2135d34f-c894-4c5b-960d-9aa792ae47ec?catalog=dcp28&version=2022-04-07T19%3A27%3A56.851000Z"
output="3ed57d69-7b79-4bff-8726-68caab01fecc/SRR16106016_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d03c2692-c5ef-4550-add8-479dd537ea47?catalog=dcp28&version=2022-04-07T19%3A27%3A29.435000Z"
output="b4a55412-3273-4137-869f-68a93521fe25/SRR16105897_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/64558449-4695-45ac-83cf-7d7851fdf0e1?catalog=dcp28&version=2022-04-07T19%3A27%3A33.840000Z"
output="6f7164e9-6b31-4da1-bf25-e370a36247cd/SRR16105937_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/599b4823-3c57-42e6-adc0-3e5936bd5a78?catalog=dcp28&version=2022-04-07T19%3A28%3A09.762000Z"
output="6d59dd5a-dbd4-4152-8b9d-c739413f7a21/SRR16106079_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/394b223a-348b-4cd7-86bf-12c94d041af7?catalog=dcp28&version=2022-04-07T19%3A26%3A57.934000Z"
output="5973faea-848d-407a-a249-85ba85264249/SRR16105794_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c3e7fd42-949b-4889-b521-aff756496a18?catalog=dcp28&version=2022-04-07T19%3A27%3A16.461000Z"
output="58c697f6-f768-4945-a107-055de56fe6b2/SRR16105845_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e0315d4b-2558-40b8-b624-09aece227445?catalog=dcp28&version=2022-04-07T19%3A27%3A37.815000Z"
output="14972570-4961-433f-8ad2-a08faf27941f/SRR16105944_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8c060e73-ee3d-42b3-a0c6-f14d90a484e4?catalog=dcp28&version=2022-04-07T19%3A27%3A21.118000Z"
output="b1942f46-14bb-445b-a046-de970f4924e7/SRR16105877_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5a13d404-1d97-4d8d-bc88-718e7fc4d8ab?catalog=dcp28&version=2022-04-07T19%3A28%3A08.202000Z"
output="a1402ec5-dcbb-4fe0-84df-2d92e26273b9/SRR16106056_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/da22e1ab-be42-44e0-8b78-2981159e15a3?catalog=dcp28&version=2022-04-07T19%3A27%3A56.432000Z"
output="40c1e501-6c42-4d72-9326-e698be1241b3/SRR16106011_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7e662928-b900-41cb-aaad-ffb0e8e9378d?catalog=dcp28&version=2022-04-07T19%3A27%3A18.029000Z"
output="398a6d0a-dd1f-4125-8508-8dbb0439b38e/SRR16105857_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/63668df3-2e4d-49cb-8c38-b71c80c16da6?catalog=dcp28&version=2022-04-07T19%3A27%3A19.962000Z"
output="92c8a58a-35fe-4b44-96ab-f6305dd8eaab/SRR16105870_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/83dc149a-46f2-431d-935c-6a2a50d32c9b?catalog=dcp28&version=2022-04-07T19%3A26%3A56.185000Z"
output="0dab1345-3f9c-45c6-a429-671708f38f52/SRR16105759_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/949172d3-5c33-4f75-bb3b-a07b21f84c73?catalog=dcp28&version=2022-04-07T19%3A28%3A12.508000Z"
output="e3beebec-9471-4d19-b4b5-370fd4e6c427/SRR16106112_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/65a21896-8fa9-4790-a0f7-837d325ceb89?catalog=dcp28&version=2022-04-07T19%3A27%3A57.783000Z"
output="8200dd65-0c24-403c-b5b5-f01fc24092d3/SRR16106026_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fa4e92f3-b7f2-4cf3-ad82-194e7e6d84a0?catalog=dcp28&version=2022-04-07T19%3A28%3A11.575000Z"
output="cc0a9e54-c45e-4065-a662-fdeb71001fc6/SRR16106097_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7cd0e697-de26-450c-b6ec-5e2c28294533?catalog=dcp28&version=2022-04-07T19%3A27%3A57.369000Z"
output="8de871f4-4a62-4667-b5a0-59e8648d9a10/SRR16106021_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/09396723-f699-4d4f-8f84-58eb7eb5f756?catalog=dcp28&version=2022-04-07T19%3A27%3A27.584000Z"
output="8f6dec87-e785-4575-b8d6-e6418f5c7133/SRR16105886_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fbc5ad05-73b4-434b-a99c-32dc5f36b97f?catalog=dcp28&version=2022-04-07T19%3A27%3A40.618000Z"
output="c71a8645-5e08-44c1-829c-b03d26855b48/SRR16105946_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/142d3f4b-fa2b-431a-9978-0e8a3563f569?catalog=dcp28&version=2022-04-07T19%3A26%3A59.032000Z"
output="beda1d88-0684-4e64-92c9-3b06f44a5e73/SRR16105817_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5aa7204e-8ae3-433e-a3d5-25f2c7690b88?catalog=dcp28&version=2022-04-07T19%3A27%3A17.571000Z"
output="ac86fd53-27a1-415f-9aa4-1889967604cc/SRR16105854_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fa48ab7b-4e4f-45ad-83e9-a57ad3405c38?catalog=dcp28&version=2022-04-07T19%3A27%3A17.318000Z"
output="11b42c9c-454b-4313-b996-09d5c32dc89c/SRR16105852_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/eaa6bfe0-6f69-474b-ad50-9da16ac52227?catalog=dcp28&version=2022-04-07T19%3A26%3A57.523000Z"
output="f884ff14-7e0e-407e-9992-998bd918d5ec/SRR16105787_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6745ec9c-c3e7-4a2f-a0f0-fe0132bca7b5?catalog=dcp28&version=2022-04-07T19%3A27%3A45.820000Z"
output="76767309-75fa-48e7-82da-f8106341bfcd/SRR16105980_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/78498791-e9b6-4d2c-9c93-298d05c3d189?catalog=dcp28&version=2022-04-07T19%3A26%3A56.704000Z"
output="5d12fe38-12a4-4f00-af18-b902d081624b/SRR16105772_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/70ca69e2-957c-4e5a-b5fb-2fd28216097d?catalog=dcp28&version=2022-04-07T19%3A27%3A05.350000Z"
output="49038b69-6ccd-4eff-bb48-988fc48c8038/SRR16105832_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/04eef0ad-4b4c-4ed1-a563-c7ef32ae4ab7?catalog=dcp28&version=2022-04-07T19%3A27%3A54.497000Z"
output="f3303ed5-9cd3-4349-931d-3767f2f0eba0/SRR16105997_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/773533ae-8620-417e-bcd4-0db2caa1a3aa?catalog=dcp28&version=2022-04-07T19%3A28%3A12.037000Z"
output="75a57b77-1132-4295-b330-740184eb9b15/SRR16106103_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/90f1aa4c-ab7b-41ff-b1e3-13e14451bff0?catalog=dcp28&version=2022-04-07T19%3A27%3A42.893000Z"
output="8f54e440-8491-473d-a01b-5e47dc6b6210/SRR16105957_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d66a44ca-fa8b-4f77-a9e6-dc1617e42567?catalog=dcp28&version=2022-04-07T19%3A28%3A00.609000Z"
output="f28f7f6f-87b3-48ca-b441-b24447ef1f58/SRR16106036_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cba81f48-c7bd-4a0a-988f-7ace7d419389?catalog=dcp28&version=2022-04-07T19%3A27%3A07.833000Z"
output="cd97de50-ba1b-42e3-ae2f-8e34a90eb766/SRR16105835_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/249aa006-05c0-413a-a1c9-08465cc14b22?catalog=dcp28&version=2022-04-07T19%3A27%3A46.015000Z"
output="167ab68e-567a-410e-bcf0-88519336d72c/SRR16105982_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1cf0da96-bd8e-4205-b40d-72344245c883?catalog=dcp28&version=2022-04-07T19%3A27%3A27.608000Z"
output="8f6dec87-e785-4575-b8d6-e6418f5c7133/SRR16105886_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3648967f-a2c6-419a-ac13-38475ac1f8a5?catalog=dcp28&version=2022-04-07T19%3A26%3A57.739000Z"
output="6691873d-a57d-4be8-bab0-27a53d83c0d9/SRR16105792_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c57db2fe-416e-48c0-9d6f-67f92eb8daf5?catalog=dcp28&version=2022-04-07T19%3A27%3A55.266000Z"
output="f2c687f8-b12c-46a2-815b-08329f279144/SRR16106003_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a6d17c91-8bd7-469c-9948-d7e955b74f59?catalog=dcp28&version=2022-04-07T19%3A27%3A57.580000Z"
output="41fceb09-b7c8-40ce-b2d9-20eda5cbf63d/SRR16106023_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/171dd1d2-d4f5-43e0-aaec-b1b067f82a02?catalog=dcp28&version=2022-04-07T19%3A27%3A43.615000Z"
output="b053b90f-9396-4c5d-ae9d-76876452d688/SRR16105962_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/979a0aff-0cad-40c8-9fce-c51b94a3367d?catalog=dcp28&version=2022-04-07T19%3A27%3A32.843000Z"
output="b42b17c1-f6c8-4ec5-a4de-0373439e383f/SRR16105927_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/087977ec-71c8-4a05-bf8f-7d86c3858a6f?catalog=dcp28&version=2022-04-07T19%3A28%3A11.132000Z"
output="94662222-bc39-4187-870e-a1d467c95b98/SRR16106091_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08190cc5-e5ba-4b8f-bfc3-db22d314e18b?catalog=dcp28&version=2022-04-07T19%3A27%3A18.789000Z"
output="4f1e110d-76b3-4ede-bd03-1a1b7a5060ba/SRR16105863_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/00db526b-d0b2-4ef1-b527-43edf5ee2128?catalog=dcp28&version=2022-04-07T19%3A26%3A57.982000Z"
output="4f1b8e71-7586-4917-8831-f1229bb25c5a/SRR16105796_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fba147d2-9c06-4bfc-9b34-ea6b598b374d?catalog=dcp28&version=2022-04-07T19%3A28%3A12.413000Z"
output="714f1455-b491-4644-be6a-31331c89e459/SRR16106109_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d45edfd5-ea81-480a-906e-5e1e0740722e?catalog=dcp28&version=2022-04-07T19%3A27%3A30.223000Z"
output="9b1691c2-52da-45a0-abe4-5b6de8955aee/SRR16105905_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6fa884b7-77bd-4fd6-89e1-54f92be77a5e?catalog=dcp28&version=2022-04-07T19%3A27%3A54.667000Z"
output="b9e3f9f0-8005-4355-ae10-20bc84286c6c/SRR16105999_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c6e9ab42-238f-4cd5-a9fc-c24dae0bc7d8?catalog=dcp28&version=2022-04-07T19%3A28%3A11.368000Z"
output="61807d1b-c7d0-4c56-be14-7d24ea2b9296/SRR16106094_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6d7a4071-7542-4b36-a7f4-055322599098?catalog=dcp28&version=2022-04-07T19%3A27%3A06.642000Z"
output="3ddbd8a5-3306-438c-a45f-a47f6315efd9/SRR16105833_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3808ab62-179a-43bd-9de5-1a4cf6b4a279?catalog=dcp28&version=2022-04-07T19%3A28%3A08.737000Z"
output="2200a288-6638-4165-89b7-1bd117e66617/SRR16106065_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e9e375e0-06a9-4dc4-98cb-f5bdf4c6bd47?catalog=dcp28&version=2022-04-07T19%3A26%3A57.840000Z"
output="f4f1f564-781d-46a4-93b1-098c0b919e29/SRR16105793_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7f98664e-a7eb-453e-bc1c-77061cf05b82?catalog=dcp28&version=2022-04-07T19%3A26%3A58.921000Z"
output="ada83954-9c04-42b3-9bb9-9c0b23070fd6/SRR16105815_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/de1642bf-fe5b-40d5-9856-14926b3a75ae?catalog=dcp28&version=2022-04-07T19%3A26%3A58.253000Z"
output="51699d38-4e97-49a0-aa75-fa27901b3f02/SRR16105803_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c4a5017-4f68-4744-844c-812b3c6abd33?catalog=dcp28&version=2022-04-07T19%3A26%3A56.248000Z"
output="1371b4ed-f5af-49bb-a96e-1ccfca16cad0/SRR16105760_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/78648e14-6a9c-4f96-8ea8-2aa130208dac?catalog=dcp28&version=2022-04-07T19%3A27%3A31.606000Z"
output="3ea625cc-c21a-4dd4-a6b3-4ef07dd06fe5/SRR16105914_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/26a5161f-effc-4092-b2f9-418f510a56a3?catalog=dcp28&version=2022-04-07T19%3A28%3A12.285000Z"
output="56842abf-71b1-4f34-9655-65587315944c/SRR16106106_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/927ad490-6f1c-4c0b-809b-3feb468d4e5a?catalog=dcp28&version=2022-04-07T19%3A28%3A11.015000Z"
output="d931e4f2-33e9-4233-9502-1dfd77a21d8c/SRR16106090_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d7e1fb57-2029-4f06-b1ca-b0625ce9ddf8?catalog=dcp28&version=2022-04-07T19%3A28%3A01.216000Z"
output="0f11ebc1-e6bc-4039-a9b5-74170fe9744f/SRR16106042_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/13e21f36-6611-4bb4-9bc0-8241fc15b82c?catalog=dcp28&version=2022-04-07T19%3A27%3A45.394000Z"
output="69a82e8c-b336-48ba-aef6-d019a36b8152/SRR16105977_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1427aa3f-8cf2-4be9-868b-c214c5c46ac3?catalog=dcp28&version=2022-04-07T19%3A26%3A58.861000Z"
output="e74ab0d6-5b8f-4955-afbe-d56fd5d095b8/SRR16105814_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d9a0593b-cafc-4dfb-9be7-723f04814d5d?catalog=dcp28&version=2022-04-07T19%3A27%3A31.321000Z"
output="37646cd9-5845-4aa3-ba6a-d1cebddd0972/SRR16105913_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f3e152b1-2c3b-4601-a1c2-8c8ee93a03cc?catalog=dcp28&version=2022-04-07T19%3A28%3A09.738000Z"
output="6d59dd5a-dbd4-4152-8b9d-c739413f7a21/SRR16106079_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e931af4d-6370-4d58-8f64-67bb7f5e2c03?catalog=dcp28&version=2022-04-07T19%3A26%3A58.341000Z"
output="7bec011d-f68f-4825-857b-e3a25b76891e/SRR16105805_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/167db47b-f03f-4e44-b0db-9e6128af2227?catalog=dcp28&version=2022-04-07T19%3A27%3A55.551000Z"
output="608f4800-5e5f-4358-9043-c6bcd2b34562/SRR16106005_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9415c37a-c917-4a6a-a38a-957afb92c001?catalog=dcp28&version=2022-04-07T19%3A26%3A56.764000Z"
output="e7f33f30-581f-4a1d-be0c-1520c6ec60f2/SRR16105773_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/09325481-8b70-4b94-8f57-bb9b74e90214?catalog=dcp28&version=2022-04-07T19%3A26%3A58.102000Z"
output="e69d2b80-9131-4af7-addb-2403890cd6ab/SRR16105799_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0de4080a-f588-46d2-9de9-59ff47b21b15?catalog=dcp28&version=2022-04-07T19%3A27%3A29.322000Z"
output="fa0de6b6-c530-4a21-b41d-ca8c94299717/SRR16105896_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4e0d6ce9-5932-4718-8960-48eaaa3a0e93?catalog=dcp28&version=2022-04-07T19%3A27%3A55.714000Z"
output="6a8bd0c5-b373-47fd-ac70-93d666ac6dd7/SRR16106006_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7917ba9f-832e-46a4-82c0-3eb1c81b8b73?catalog=dcp28&version=2022-04-07T19%3A27%3A16.730000Z"
output="75cb8029-0e19-47bb-a782-e9f4e89dfb09/SRR16105847_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/77ddf0da-d35e-4341-97aa-10eb05c9067a?catalog=dcp28&version=2022-04-07T19%3A27%3A04.156000Z"
output="339859d9-009d-4f94-9a39-5e1e79108ec8/SRR16105831_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/43eb395f-936d-4583-9aa2-960458d69531?catalog=dcp28&version=2022-04-07T19%3A27%3A31.962000Z"
output="0386a58f-f2a9-4a8d-b0a5-1f5e954bcbd7/SRR16105918_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5a8aee6b-82ba-4e54-a1b9-f92292c23e78?catalog=dcp28&version=2022-04-07T19%3A27%3A20.133000Z"
output="ff4c95fb-f0d3-4f3c-a147-37f48b2040b0/SRR16105871_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3c866c46-de81-4015-b86e-0b1e990a10ff?catalog=dcp28&version=2022-04-07T19%3A27%3A18.422000Z"
output="a256c6e1-278c-43cd-a863-818f1f6866da/SRR16105861_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4595a8e5-00f8-4fdf-bd2e-b53a4c58b057?catalog=dcp28&version=2022-04-07T19%3A26%3A57.546000Z"
output="51d16b92-563a-40eb-9ceb-d7338bd7de8b/SRR16105788_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0cf4e516-74f0-4b30-8140-2e3caa0607ec?catalog=dcp28&version=2022-04-07T19%3A26%3A58.204000Z"
output="5d12037a-0a50-421c-84e0-367c12f41b55/SRR16105801_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1c3c2a91-e7dd-4528-a630-8c6b2118159e?catalog=dcp28&version=2022-04-07T19%3A26%3A59.047000Z"
output="beda1d88-0684-4e64-92c9-3b06f44a5e73/SRR16105817_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/61e8802b-5058-453c-ae79-bd62e88bf582?catalog=dcp28&version=2022-04-07T19%3A27%3A57.110000Z"
output="ef5f0bda-99b4-4dda-97bf-a986febb7166/SRR16106018_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/90d907d5-6af1-4af8-809c-99a7648211eb?catalog=dcp28&version=2022-04-07T19%3A28%3A09.446000Z"
output="d2749e92-59b1-4bf8-a5aa-bf79ab36a671/SRR16106075_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ac16c086-0bbb-4a1f-9aaa-b7f14ad4d694?catalog=dcp28&version=2022-04-07T19%3A27%3A33.345000Z"
output="9a1699a3-b337-452b-8a88-b47b3d9cc44f/SRR16105932_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dd6ebcee-31cc-485b-a73e-83668f8e0cbf?catalog=dcp28&version=2022-04-07T19%3A27%3A56.062000Z"
output="b1211531-2be2-448b-b806-e137b07d779c/SRR16106008_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/792cccae-b4d5-454a-8896-fe3081c453d2?catalog=dcp28&version=2022-04-07T19%3A27%3A42.558000Z"
output="45ebc9fb-89e0-4bfa-9a27-56c915f6e58b/SRR16105953_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ef2dbee2-cdb7-456a-9e18-d8482af67b6e?catalog=dcp28&version=2022-04-07T19%3A27%3A29.691000Z"
output="81817ea5-b474-4514-b789-e593e7211b16/SRR16105899_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d7db00e3-3a73-4f21-94dc-71c290907fab?catalog=dcp28&version=2022-04-07T19%3A26%3A58.291000Z"
output="34a12e21-0d7d-40e5-9e02-2e303ee76eed/SRR16105804_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/818f19c6-a3cc-4820-ae6e-08554c87ffc4?catalog=dcp28&version=2022-04-07T19%3A28%3A07.114000Z"
output="0d7cc23a-8b6b-43a8-8621-4ba22fb36774/SRR16106049_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ce52a15d-6779-4060-a28f-4e6b87cf0a10?catalog=dcp28&version=2022-04-07T19%3A26%3A58.688000Z"
output="9b8aca24-d1fe-4c91-b144-98225db0ac0b/SRR16105810_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f6a557b5-fc9f-485f-a9ed-c2310c5fe843?catalog=dcp28&version=2022-04-07T19%3A26%3A56.450000Z"
output="6bf6781c-1dd4-4f8a-a4c4-7314cbe642f0/SRR16105765_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b7128adf-b3ee-4973-bd99-e7f81158fadd?catalog=dcp28&version=2022-04-07T19%3A27%3A28.766000Z"
output="7f951a6e-5541-45d8-bca2-ca3477480664/SRR16105893_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/332f0de0-394d-45fb-b11f-8f7390ed6534?catalog=dcp28&version=2022-04-07T19%3A27%3A56.135000Z"
output="c5e014da-2cc7-448e-89eb-e0720cd21f61/SRR16106009_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2dacba64-f814-4328-81e8-6086c5537218?catalog=dcp28&version=2022-04-07T19%3A27%3A44.378000Z"
output="bd3b5bfa-bb91-4a09-8737-67ac1da7af2f/SRR16105969_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/44930e3c-af96-4129-be8d-fc9c982d26e1?catalog=dcp28&version=2022-04-07T19%3A28%3A11.972000Z"
output="7b142e78-0ab7-40c0-9b1b-0ffe9ecf0582/SRR16106102_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2deb663f-0436-46a0-9a9c-2bb5c010b5ae?catalog=dcp28&version=2022-04-07T19%3A27%3A16.001000Z"
output="76722270-1b19-4a3d-a588-6747d894cab0/SRR16105841_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/180861bb-445d-48ea-bee8-4006d2534d58?catalog=dcp28&version=2022-04-07T19%3A28%3A09.423000Z"
output="2c9e75b6-f9fa-453f-9caa-e445e50c2e5d/SRR16106074_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2909812f-8589-4514-b30f-30bb808bc83d?catalog=dcp28&version=2022-04-07T19%3A27%3A21.450000Z"
output="2bee19a1-6841-4871-9c36-73f1f29349f9/SRR16105880_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7a4c0c5d-0a52-4f2d-b88c-bbd15f463bc9?catalog=dcp28&version=2022-04-07T19%3A27%3A32.062000Z"
output="1dc08504-d51f-4e75-be9d-90d9ee5c76ac/SRR16105919_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/012219e1-8902-4943-a00a-e5c440d8e6ab?catalog=dcp28&version=2022-04-07T19%3A27%3A18.175000Z"
output="74d703e4-3167-4670-8f16-86007d947783/SRR16105859_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/85f6ced6-e6a4-4a5a-b5e5-2fce2db9aa85?catalog=dcp28&version=2022-04-07T19%3A26%3A58.058000Z"
output="88855126-fc0c-480f-822b-0ff3779c92bd/SRR16105798_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2616b47b-cd97-4e9e-9326-90ce805f7be3?catalog=dcp28&version=2022-04-07T19%3A28%3A08.786000Z"
output="70abaeed-cb70-450c-9527-914ea48bf443/SRR16106066_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a0308969-cc0d-4834-9be3-82d5ad96cb65?catalog=dcp28&version=2022-04-07T19%3A27%3A33.298000Z"
output="86b2c520-0be0-499c-8394-efecce2ae800/SRR16105931_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/447a2840-d254-4201-8d25-1b59143f52c0?catalog=dcp28&version=2022-04-07T19%3A27%3A17.792000Z"
output="967d1938-e695-43f5-ba5c-f4d796a9c84f/SRR16105855_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bab3465f-82c8-4213-8fb6-1669ba7058b6?catalog=dcp28&version=2022-04-07T19%3A27%3A34.068000Z"
output="68441aaf-1e11-4e56-b2b4-4823b0c61093/SRR16105938_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fee310ff-0a57-4ffc-b5f3-f9165ffd8114?catalog=dcp28&version=2022-04-07T19%3A27%3A43.119000Z"
output="d7f2c949-dffb-46cb-90e1-69506f812ddb/SRR16105959_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5a26742a-d337-4be3-bccb-4844e45eced0?catalog=dcp28&version=2022-04-07T19%3A27%3A21.297000Z"
output="750ee074-c01f-4378-bea9-53e746bf1b07/SRR16105879_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a461c050-a3f2-421a-b822-f8120fb6e8ee?catalog=dcp28&version=2022-04-07T19%3A27%3A59.106000Z"
output="aee6026d-07c1-47f7-b443-b31d4ddf4e26/SRR16106034_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4ccda3a9-ac59-4eb0-93b7-cbb90f7c886d?catalog=dcp28&version=2022-04-07T19%3A28%3A10.240000Z"
output="8ad0eecd-61c4-4eb3-8201-6d72def553d6/SRR16106086_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6c7ce4cd-e9af-4982-b801-5653132d95a2?catalog=dcp28&version=2022-04-07T19%3A26%3A56.678000Z"
output="57e79970-7e14-43b7-8501-905f66922f9b/SRR16105771_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c7d47cd3-49d3-4cfb-87f8-ba87a97b9dc7?catalog=dcp28&version=2022-04-07T19%3A28%3A11.746000Z"
output="23b42a69-274c-41f6-acd4-a466732254ac/SRR16106099_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e4783e1a-b519-4ae5-b19a-4b5274f28624?catalog=dcp28&version=2022-04-07T19%3A27%3A46.074000Z"
output="167ab68e-567a-410e-bcf0-88519336d72c/SRR16105982_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2965b4be-1778-488f-93d4-468e76bf9e1b?catalog=dcp28&version=2022-04-07T19%3A27%3A44.156000Z"
output="ac7679e6-c824-462c-b88c-3dc1f5b42b47/SRR16105966_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8f3d57da-e60f-4e8e-a3ef-0e3cce7284a0?catalog=dcp28&version=2022-04-07T19%3A28%3A07.372000Z"
output="db2ac85a-6c6c-4f1b-a7bc-8eaf8b1fd124/SRR16106050_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b9fb8ec0-4c61-4360-9f76-f94802639007?catalog=dcp28&version=2022-04-07T19%3A27%3A30.336000Z"
output="ba60e59f-5da9-4f60-bd15-4186281ce060/SRR16105906_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e2b02f7c-e52b-4167-9dc5-c4a8c0edd6a4?catalog=dcp28&version=2022-04-07T19%3A27%3A09.306000Z"
output="ae48556e-60dc-4ad4-9096-e2421da4586c/SRR16105836_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b7401d9b-6ab0-43d6-a048-508a4a62fe4d?catalog=dcp28&version=2022-04-07T19%3A27%3A11.911000Z"
output="8f305642-c861-49fb-a8d0-05b3ef0396f8/SRR16105837_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7b5a1310-64b4-46fa-aca0-29179ec1e4f8?catalog=dcp28&version=2022-04-07T19%3A27%3A42.765000Z"
output="f97d049e-dcbd-4d1a-9349-704cd1edd1fb/SRR16105955_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/670542e0-df08-4d33-bf3c-3956ec0cbea5?catalog=dcp28&version=2022-04-07T19%3A27%3A28.994000Z"
output="9b63f70e-9439-43d7-ae2b-ab46ec441c32/SRR16105894_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1f1a0d4f-e1d5-4a92-be5e-0dee62babe00?catalog=dcp28&version=2022-04-07T19%3A27%3A55.857000Z"
output="7787e4b9-1cbc-417c-b4e5-ce0f8ef76eb6/SRR16106007_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e969aee5-dd4a-40c3-8127-419010c5762f?catalog=dcp28&version=2022-04-07T19%3A27%3A19.235000Z"
output="941885c8-4d6c-4824-bdc2-a61c29e1251e/SRR16105865_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6af000f4-84bc-4960-ba5e-0c09c7aebb1a?catalog=dcp28&version=2022-04-07T19%3A27%3A43.055000Z"
output="3d2aebd8-a4e0-44fb-8037-b6a1a02fed9a/SRR16105958_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/eddf5ca3-4ee4-4188-befb-16c4b603b9cf?catalog=dcp28&version=2022-04-07T19%3A26%3A59.177000Z"
output="ef00f9c9-7d95-43e7-98cd-7e12fba5156e/SRR16105819_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/85ea686d-e568-4953-a958-50d3ba7b3047?catalog=dcp28&version=2022-04-07T19%3A26%3A59.206000Z"
output="d8c88a8a-45e9-48cb-9dee-529409a3e2f5/SRR16105820_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/43001ef1-6777-4c72-b10a-0e41a328bcd6?catalog=dcp28&version=2022-04-07T19%3A26%3A56.085000Z"
output="b02a047d-33bf-4a58-b920-2a296516f007/SRR16105756_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d3672e49-ceb8-422e-8c06-74378aea04d6?catalog=dcp28&version=2022-04-07T19%3A28%3A00.891000Z"
output="54d67cd1-84f2-4b4a-bbe4-9b938cef55ee/SRR16106039_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/eaf4aba5-abb7-4764-82ec-ca6df6c3d03a?catalog=dcp28&version=2022-04-07T19%3A27%3A52.971000Z"
output="16e9ea04-bc15-4d39-8bce-5ab6c3d1a773/SRR16105992_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/56e9f006-a816-4103-87ce-1796c7e2aebf?catalog=dcp28&version=2022-04-07T19%3A26%3A59.742000Z"
output="2629e260-5903-478b-a39e-59708cf2052f/SRR16105827_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8b8d50a6-f506-4fdc-ac1a-bd2135f9700b?catalog=dcp28&version=2022-04-07T19%3A27%3A06.966000Z"
output="ce6d1e9b-d8d7-4a65-9f0f-869665816f2d/SRR16105834_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f3b4c9b2-9112-4d04-a50d-5ae4cf7fb602?catalog=dcp28&version=2022-04-07T19%3A28%3A11.795000Z"
output="23b42a69-274c-41f6-acd4-a466732254ac/SRR16106099_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/216e8ef8-0ffb-4183-a133-8ba0d8cad589?catalog=dcp28&version=2022-04-07T19%3A27%3A44.870000Z"
output="f575dc89-29eb-4c14-9951-03903f35551f/SRR16105973_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/26a34aec-2366-4281-b6a2-d1f5d13c63f7?catalog=dcp28&version=2022-04-07T19%3A26%3A56.948000Z"
output="fe2e00d7-e6ff-4f11-a376-da60874a7924/SRR16105776_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6fb7ee21-11ed-46aa-877e-c3037d491499?catalog=dcp28&version=2022-04-07T19%3A27%3A07.320000Z"
output="ce6d1e9b-d8d7-4a65-9f0f-869665816f2d/SRR16105834_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1aa52f8f-ec17-4d28-974d-65e1c44f60a8?catalog=dcp28&version=2022-04-07T19%3A26%3A56.146000Z"
output="d06b69d0-e91e-499c-8ce8-038faec09094/SRR16105758_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/75616a56-0d2c-45a4-bc5e-a3cfad338ac7?catalog=dcp28&version=2022-04-07T19%3A28%3A12.082000Z"
output="75a57b77-1132-4295-b330-740184eb9b15/SRR16106103_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8569ee64-1e1d-49d4-b47e-9b6376b94a9a?catalog=dcp28&version=2022-04-07T19%3A27%3A17.454000Z"
output="11b42c9c-454b-4313-b996-09d5c32dc89c/SRR16105852_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1e730240-0562-4d2e-b9a2-83ccf6666b36?catalog=dcp28&version=2022-04-07T19%3A27%3A16.060000Z"
output="0d01ab46-8ff9-4649-ac7d-c89375ea8d20/SRR16105842_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2336f6bf-0632-48c3-86eb-bb31cb8c2572?catalog=dcp28&version=2022-04-07T19%3A28%3A01.030000Z"
output="9781bbc9-74e7-4d79-94d6-0d46774211eb/SRR16106041_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0f58c461-95b7-45e5-9059-98f3795fe369?catalog=dcp28&version=2022-04-07T19%3A28%3A08.325000Z"
output="524efc57-19c1-4878-b2a3-c360f140d4f9/SRR16106057_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6bc795d9-6663-4106-ae3f-81e13b71c858?catalog=dcp28&version=2022-04-07T19%3A27%3A17.893000Z"
output="f9f906cb-3cf3-442d-b264-17b53181fee3/SRR16105856_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/695ed2ca-8ce4-4159-8864-b38ecf95b8e4?catalog=dcp28&version=2022-04-07T19%3A26%3A59.157000Z"
output="ef00f9c9-7d95-43e7-98cd-7e12fba5156e/SRR16105819_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d61ea429-57d5-4171-a998-4137e2ac6f4a?catalog=dcp28&version=2022-04-07T19%3A27%3A30.137000Z"
output="4e0e7092-b395-4524-818f-d294a98e2fa9/SRR16105904_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4e626471-366e-42f9-9852-b90aeb166e2a?catalog=dcp28&version=2022-04-07T19%3A27%3A32.030000Z"
output="1dc08504-d51f-4e75-be9d-90d9ee5c76ac/SRR16105919_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/326e3897-f12b-4eb3-a937-a45e4e9043e1?catalog=dcp28&version=2022-04-07T19%3A27%3A33.663000Z"
output="783fc31c-c3fd-44dc-9279-abf3c60b2dc8/SRR16105935_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0c7f6b68-f654-4ff2-85c8-ad10ba98230f?catalog=dcp28&version=2022-04-07T19%3A27%3A17.552000Z"
output="fad17bc2-c861-4f55-aa68-32f9410d9c99/SRR16105853_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4da64a54-930f-49e0-b014-bfe79eac5eea?catalog=dcp28&version=2022-04-07T19%3A26%3A58.371000Z"
output="ee1a5d8f-b801-4f53-8ef4-a2840105e89a/SRR16105806_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4d8a658b-59c3-4d75-9e7f-313afef30722?catalog=dcp28&version=2022-04-07T19%3A27%3A33.114000Z"
output="70a9dad1-5a6b-42ec-b62e-43050327e97d/SRR16105930_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6bce4f1b-d3fa-4547-a826-87517329bf48?catalog=dcp28&version=2022-04-07T19%3A27%3A28.276000Z"
output="f92ab2be-b16d-49d5-9dd6-64a53d44a5f8/SRR16105890_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ebb4cdba-d32a-4feb-ac74-5b3c585c603e?catalog=dcp28&version=2022-04-07T19%3A28%3A10.332000Z"
output="8396361d-c7d1-4f3d-ae60-b9b1da6a76ce/SRR16106087_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c2c35720-f3fc-413f-8d77-5002e1a984f7?catalog=dcp28&version=2022-04-07T19%3A27%3A20.547000Z"
output="d0641426-1fc5-42ac-815f-604ddad42dfc/SRR16105873_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7a0f855d-8a42-41ee-bb39-beb52097deda?catalog=dcp28&version=2022-04-07T19%3A27%3A27.437000Z"
output="fb0e10ac-3443-4fad-a6fd-53dd612610a7/SRR16105885_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5212fda2-9fed-4abb-a8b8-1fdf58e98003?catalog=dcp28&version=2022-04-07T19%3A28%3A12.018000Z"
output="75a57b77-1132-4295-b330-740184eb9b15/SRR16106103_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/249a8720-d30b-4c38-a585-f66244d1ae95?catalog=dcp28&version=2022-04-07T19%3A27%3A57.703000Z"
output="584cbf84-929a-4d8a-acd4-606ecff0694c/SRR16106025_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2399c7bf-12e3-4a3d-ade8-c2b40a2feb16?catalog=dcp28&version=2022-04-07T19%3A28%3A09.667000Z"
output="35059cf0-2e3e-470d-9169-7b7cbe64e56a/SRR16106078_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/45dbc317-b0e8-4985-bfe2-78f607c0126b?catalog=dcp28&version=2022-04-07T19%3A28%3A00.700000Z"
output="5e12184a-b091-47a1-9db9-d9174f25dce8/SRR16106037_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b62af403-0424-46db-9a4e-e90d7ce2f5f7?catalog=dcp28&version=2022-04-07T19%3A27%3A48.835000Z"
output="38e0effd-67eb-4f48-8847-71c423a6ef28/SRR16105987_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5b1d94b6-8f56-456e-94ea-976de84d3477?catalog=dcp28&version=2022-04-07T19%3A28%3A12.544000Z"
output="8a15abfd-b0db-4222-b59c-6032a0dced1a/SRR16106113_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0f6d1e3c-6386-4a4d-801a-3dd84781b2eb?catalog=dcp28&version=2022-04-07T19%3A27%3A36.149000Z"
output="ba6d0a59-079c-4cac-8d44-1777c77d2e07/SRR16105940_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7049511a-3631-486c-aa38-ec9771ded41d?catalog=dcp28&version=2022-04-07T19%3A27%3A19.627000Z"
output="1d66e5bd-d41e-47c2-b825-8ca45d02813f/SRR16105868_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ec6d5bfe-b56c-447e-96be-dbdceabf35f7?catalog=dcp28&version=2022-04-07T19%3A27%3A57.926000Z"
output="da6cf693-ad4d-440a-a0e7-698653151e44/SRR16106028_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/599bb087-a83e-47bd-b96e-d8ccfb6cc630?catalog=dcp28&version=2022-04-07T19%3A28%3A00.823000Z"
output="bd3f8f43-09c9-4df0-8ce5-0f57f98f1c3a/SRR16106038_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6b140c6d-15b2-4137-8cbb-482010ddc8b4?catalog=dcp28&version=2022-04-07T19%3A26%3A57.242000Z"
output="8df20e18-d035-4b7a-8e04-89a3522d2494/SRR16105781_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/25b58ef0-a64e-4926-b4b1-cbb3d9f1ebc5?catalog=dcp28&version=2022-04-07T19%3A27%3A20.794000Z"
output="6d41648e-e6bb-4b77-924f-beae862055d0/SRR16105875_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f26be57f-c330-4807-82a4-e6c53ec7d393?catalog=dcp28&version=2022-04-07T19%3A28%3A09.936000Z"
output="e1f958f3-7f7d-41d0-8551-a82103e09c4d/SRR16106082_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5d8cb76e-0b5f-4e9b-b21d-9c8dc7ab78d1?catalog=dcp28&version=2022-04-07T19%3A27%3A31.467000Z"
output="37646cd9-5845-4aa3-ba6a-d1cebddd0972/SRR16105913_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7558b22d-b635-47ff-853e-950e28d50175?catalog=dcp28&version=2022-04-07T19%3A27%3A56.647000Z"
output="4f14f89d-2083-4b95-b5b2-10e20b80484b/SRR16106013_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7d53d7f2-a288-44e2-be7a-55068ffa139f?catalog=dcp28&version=2022-04-07T19%3A27%3A44.070000Z"
output="953638a3-828c-4db4-a9b2-85149907861f/SRR16105965_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/eabc0e51-493e-41ec-88d1-3c4e926053db?catalog=dcp28&version=2022-04-07T19%3A28%3A09.177000Z"
output="e002d41a-66bf-47cf-9ff2-c5a18a2ac848/SRR16106071_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dee0ad95-da5f-4bf7-8c9c-34c8bb6eaec5?catalog=dcp28&version=2022-04-07T19%3A27%3A42.620000Z"
output="d9e39c80-264e-44ec-81fc-c86f430742c3/SRR16105954_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1c5cb71e-fe6f-40d3-ab41-e8ef504c0c2e?catalog=dcp28&version=2022-04-07T19%3A28%3A11.348000Z"
output="61807d1b-c7d0-4c56-be14-7d24ea2b9296/SRR16106094_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/19797f8e-c3f2-4efc-8cd7-45f528bf6f1a?catalog=dcp28&version=2022-04-07T19%3A26%3A57.218000Z"
output="2407f163-90e5-4aad-8944-837e4f541a74/SRR16105780_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a12e0a6f-93df-466d-84ef-fe8d6bf0788a?catalog=dcp28&version=2022-04-07T19%3A28%3A09.582000Z"
output="d56edd59-ff53-43c3-bc73-97d1b9fce3d2/SRR16106077_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/79c7976c-d177-492a-8b3f-116d205b28e8?catalog=dcp28&version=2022-04-07T19%3A27%3A45.532000Z"
output="ac214f2f-64cb-45be-bcd8-1957b48ea0c8/SRR16105978_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/53228a63-7384-4b6d-b40d-0aa846378c60?catalog=dcp28&version=2022-04-07T19%3A27%3A20.942000Z"
output="13f4f451-c38a-48d8-945e-282e3f01c50d/SRR16105876_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e1e10c39-36c0-4d00-99e6-a93fd323bd62?catalog=dcp28&version=2022-04-07T19%3A28%3A00.854000Z"
output="54d67cd1-84f2-4b4a-bbe4-9b938cef55ee/SRR16106039_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2fc0488e-75ee-468e-ae0c-10eaa07deb34?catalog=dcp28&version=2022-04-07T19%3A27%3A34.996000Z"
output="38dedfdf-d9f5-4e8c-b49a-58960a26b9f0/SRR16105939_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bf48badd-418b-4784-b737-50397eda41c4?catalog=dcp28&version=2022-04-07T19%3A26%3A56.592000Z"
output="6190457d-00eb-41cb-b11e-c6e06604f58f/SRR16105769_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/799e193c-0a5b-47b5-9b3c-db3358889085?catalog=dcp28&version=2022-04-07T19%3A27%3A32.317000Z"
output="536b9433-54d3-4fb5-a9cc-f408eb3f9ba9/SRR16105922_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c94f5b7-893e-42d9-afb7-126ed3dbef9f?catalog=dcp28&version=2022-04-07T19%3A27%3A19.071000Z"
output="d710d243-2db1-443d-b9d5-b8079b3df6bc/SRR16105864_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/80d30695-a485-4fd0-a3f2-2a6473ae9e33?catalog=dcp28&version=2022-04-07T19%3A28%3A07.993000Z"
output="8af57556-1650-4217-a4e0-c76a67224a71/SRR16106053_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2ed69ccc-d154-4c18-83eb-d99aaf0c1cdc?catalog=dcp28&version=2022-04-07T19%3A26%3A58.741000Z"
output="93d9a8f6-8813-4cfa-9c37-a1447f614a47/SRR16105811_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d0c76a93-833e-40c2-b8aa-a3c3b8b4651a?catalog=dcp28&version=2022-04-07T19%3A26%3A57.754000Z"
output="6691873d-a57d-4be8-bab0-27a53d83c0d9/SRR16105792_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dc977ed3-2abc-4a1a-801d-6c1564593e43?catalog=dcp28&version=2022-04-07T19%3A27%3A33.498000Z"
output="6c955fe5-cfc0-425c-942b-8f2ccd4139c5/SRR16105934_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c318de39-0e81-4ec8-8f46-9b78ec60adb2?catalog=dcp28&version=2022-04-07T19%3A27%3A18.217000Z"
output="74d703e4-3167-4670-8f16-86007d947783/SRR16105859_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4b894551-f30b-4c47-b943-3381c2740909?catalog=dcp28&version=2022-04-07T19%3A27%3A30.419000Z"
output="5fdc2a0f-c761-48fc-9204-402011d61a06/SRR16105908_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08c8a81a-3ddf-4aa9-9a72-6f75181fdedd?catalog=dcp28&version=2022-04-07T19%3A26%3A56.566000Z"
output="31806f69-282e-40a1-9204-98ab7bd60d0f/SRR16105768_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/962c82ad-c8b1-4bde-9beb-b77f8f828f88?catalog=dcp28&version=2022-04-07T19%3A26%3A58.754000Z"
output="93d9a8f6-8813-4cfa-9c37-a1447f614a47/SRR16105811_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4a0491f0-51e9-48db-9e8d-54a0eaa6a399?catalog=dcp28&version=2022-04-07T19%3A28%3A09.562000Z"
output="41020ffc-e697-4c52-8d49-b9b3984a4338/SRR16106076_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9fe37a28-359b-46f7-8c99-4175a382358b?catalog=dcp28&version=2022-04-07T19%3A27%3A41.888000Z"
output="82ecaa87-aa59-455d-a17b-6a1b7a2c4409/SRR16105947_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/66d16453-a542-49e4-919e-273935a67f5c?catalog=dcp28&version=2022-04-07T19%3A26%3A55.981000Z"
output="00375e15-335c-4fe8-8ac1-dd456ef205bc/SRR16105753_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0f786d07-c7aa-44b4-88a0-ae7a4d1a7bd1?catalog=dcp28&version=2022-04-07T19%3A26%3A59.578000Z"
output="237910d7-064b-491a-b077-2c4ee7c52708/SRR16105825_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/165b856b-7244-421f-aa2e-3948e2940fe9?catalog=dcp28&version=2022-04-07T19%3A28%3A08.106000Z"
output="bb90f392-7e94-4cc6-b11c-8ed6b9e16dde/SRR16106055_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/47cadd6f-5d93-44f2-a0ab-2e2c0db707a7?catalog=dcp28&version=2022-04-07T19%3A28%3A08.844000Z"
output="1412c4b9-44a5-4ac4-9601-e71d23c1f949/SRR16106068_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5efccf98-6f05-4122-a0bb-ec3ffda52b6d?catalog=dcp28&version=2022-04-07T19%3A27%3A57.346000Z"
output="8de871f4-4a62-4667-b5a0-59e8648d9a10/SRR16106021_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e887d288-d1ce-42cf-8ad1-20ff809d928c?catalog=dcp28&version=2022-04-07T19%3A27%3A18.346000Z"
output="d419844e-9a75-4f20-98a9-8c6b68b6e865/SRR16105860_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/52f57be4-9ca5-4bdf-93cb-3024424e2ddc?catalog=dcp28&version=2022-04-07T19%3A27%3A01.243000Z"
output="175d983d-e177-44a6-9bcf-dbc121e48b0b/SRR16105829_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/950cb36e-173c-487b-ad65-f8e6a5b6c2d9?catalog=dcp28&version=2022-04-07T19%3A26%3A58.892000Z"
output="e74ab0d6-5b8f-4955-afbe-d56fd5d095b8/SRR16105814_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2b2e4772-b07e-44f4-9ea2-b9a3d0cf4e6b?catalog=dcp28&version=2022-04-07T19%3A28%3A12.484000Z"
output="944244ed-be4d-4d23-9686-5fd9dc627ef2/SRR16106111_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c5f8e760-3da5-43f2-861e-7081b0b281cb?catalog=dcp28&version=2022-04-07T19%3A27%3A30.833000Z"
output="9fd8eb0e-290d-45c0-b383-31370e729e8f/SRR16105911_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/874e14f5-5a16-4f17-9c45-112fa3ecb20b?catalog=dcp28&version=2022-04-07T19%3A28%3A01.335000Z"
output="3fa51f19-f8ff-46e7-8843-adc53f852b11/SRR16106044_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3bb1f1b4-c8ea-40f5-acf9-ebc24cfee2b6?catalog=dcp28&version=2022-04-07T19%3A27%3A55.518000Z"
output="c7d75ede-9c9a-483c-8695-8bea63ab971b/SRR16106004_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/de7bbb2d-d151-45a2-b50d-a0155eab331a?catalog=dcp28&version=2022-04-07T19%3A28%3A12.532000Z"
output="e3beebec-9471-4d19-b4b5-370fd4e6c427/SRR16106112_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/321543fe-450f-40cd-a85b-c0d6b18d7556?catalog=dcp28&version=2022-04-07T19%3A27%3A32.520000Z"
output="3e6f7d88-6ab6-4dfd-b4f2-1371411780a7/SRR16105924_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f1ab7685-f7de-4a1c-a663-10a22784ef60?catalog=dcp28&version=2022-04-07T19%3A27%3A33.202000Z"
output="70a9dad1-5a6b-42ec-b62e-43050327e97d/SRR16105930_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c2a74a7d-2d91-4e8b-875c-443e6f8e474f?catalog=dcp28&version=2022-04-07T19%3A26%3A56.824000Z"
output="30100aa6-2029-4446-b588-2b3dff90fcec/SRR16105775_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b982fb38-1109-42c5-b6a0-a31fde3da846?catalog=dcp28&version=2022-04-07T19%3A27%3A17.721000Z"
output="967d1938-e695-43f5-ba5c-f4d796a9c84f/SRR16105855_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fad6bdf3-f460-4443-8d7d-190c2fb2e089?catalog=dcp28&version=2022-04-07T19%3A27%3A54.254000Z"
output="84d493d1-968f-4520-892d-3331d900b8f9/SRR16105995_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a3362cf9-979b-4359-bbb1-7ce85f2e9c5b?catalog=dcp28&version=2022-04-07T19%3A27%3A29.926000Z"
output="0b237b15-1e32-4961-b572-7d184b8eff7d/SRR16105902_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ee75adc0-1444-490d-9f37-0c35b52cfceb?catalog=dcp28&version=2022-04-07T19%3A28%3A09.093000Z"
output="e002d41a-66bf-47cf-9ff2-c5a18a2ac848/SRR16106071_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fa908516-5cdc-4fc1-933a-23893d887dab?catalog=dcp28&version=2022-04-07T19%3A27%3A32.439000Z"
output="06fb0d09-a800-40b6-838d-1c20d78ecbdc/SRR16105923_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ac7c51f1-911c-4ed1-8fa2-d17101c78e8f?catalog=dcp28&version=2022-04-07T19%3A27%3A44.052000Z"
output="953638a3-828c-4db4-a9b2-85149907861f/SRR16105965_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/26c29c83-be75-4d0f-8caf-57254030764f?catalog=dcp28&version=2022-04-07T19%3A28%3A08.767000Z"
output="70abaeed-cb70-450c-9527-914ea48bf443/SRR16106066_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/25ff3e2a-b820-492b-987e-8f292687ce31?catalog=dcp28&version=2022-04-07T19%3A28%3A09.850000Z"
output="77afdd55-5dc2-444f-b63e-e5bd7d9b9c44/SRR16106081_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/db84e1ed-7ba3-47c9-bbad-1ecf6e7eb1be?catalog=dcp28&version=2022-04-07T19%3A27%3A18.315000Z"
output="d419844e-9a75-4f20-98a9-8c6b68b6e865/SRR16105860_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/979362fd-35e6-40a0-9924-ff4a3c89642d?catalog=dcp28&version=2022-04-07T19%3A27%3A48.890000Z"
output="d1ad8f6f-5d92-486f-85bf-e8cdba503351/SRR16105988_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6c37bb5d-3a77-4be3-a13e-d8aea96c5434?catalog=dcp28&version=2022-04-07T19%3A27%3A44.024000Z"
output="1e4f8657-7fd1-446e-a0ac-0fe3c567b6be/SRR16105964_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9ad36f49-0249-4d58-9893-c3c9cc0140b7?catalog=dcp28&version=2022-04-07T19%3A28%3A01.126000Z"
output="9781bbc9-74e7-4d79-94d6-0d46774211eb/SRR16106041_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9a0717cc-87ce-403f-a5e0-e6043f6c7716?catalog=dcp28&version=2022-04-07T19%3A27%3A21.237000Z"
output="685db304-d1d0-4263-806e-f1051093a1db/SRR16105878_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b944df3b-f3d5-46fb-aac0-1654c6e12d72?catalog=dcp28&version=2022-04-07T19%3A28%3A05.583000Z"
output="975d507d-3c7e-41f6-905e-93e9460d3108/SRR16106048_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/89d7dfb0-d6fb-432a-b9ed-4808c8fd741b?catalog=dcp28&version=2022-04-07T19%3A28%3A02.318000Z"
output="d6ecb457-a871-41d5-b2de-92ba4fadf9ae/SRR16106045_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/41ee6767-ffe7-4824-9a8f-5d10968ed15c?catalog=dcp28&version=2022-04-07T19%3A28%3A12.362000Z"
output="94316c6a-decf-400e-b9f1-9b2da2ee228c/SRR16106108_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e54b5e8a-9d5f-4cee-b6d5-52b0456401a1?catalog=dcp28&version=2022-04-07T19%3A26%3A58.327000Z"
output="7bec011d-f68f-4825-857b-e3a25b76891e/SRR16105805_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3e3ff6cd-9fab-435d-906f-73d3e86f217b?catalog=dcp28&version=2022-04-07T19%3A28%3A09.956000Z"
output="e1f958f3-7f7d-41d0-8551-a82103e09c4d/SRR16106082_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c14cee4b-c02a-45dc-8953-6ef1ec63cdc6?catalog=dcp28&version=2022-04-07T19%3A27%3A42.486000Z"
output="87b24f06-ecbe-4233-a1c8-ffc65f6cac25/SRR16105952_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ed74cf58-366c-427b-8d87-fbefebea159c?catalog=dcp28&version=2022-04-07T19%3A27%3A30.355000Z"
output="0098acb4-e41d-497d-b7c6-d754a1960474/SRR16105907_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d9e197f1-a32e-4848-825b-422147551218?catalog=dcp28&version=2022-04-07T19%3A27%3A30.394000Z"
output="0098acb4-e41d-497d-b7c6-d754a1960474/SRR16105907_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3812a831-01cb-49a8-9bdc-4a69eb78aecf?catalog=dcp28&version=2022-04-07T19%3A26%3A56.134000Z"
output="c639013f-3adc-4f9f-97cd-965267bca80b/SRR16105757_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d8bb890e-e067-45dd-b891-fd3104fc8b11?catalog=dcp28&version=2022-04-07T19%3A28%3A10.014000Z"
output="949468a1-494e-4a3d-939d-03322e793ff0/SRR16106083_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b488946b-1676-4670-a181-76ddf9bcbee1?catalog=dcp28&version=2022-04-07T19%3A27%3A06.050000Z"
output="3ddbd8a5-3306-438c-a45f-a47f6315efd9/SRR16105833_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9ab3d281-d50c-454f-852e-8eb1cf7324a3?catalog=dcp28&version=2022-04-07T19%3A26%3A59.606000Z"
output="237910d7-064b-491a-b077-2c4ee7c52708/SRR16105825_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/99f7aea1-b0d9-404c-9bc8-0a0c58c9f2b3?catalog=dcp28&version=2022-04-07T19%3A27%3A48.642000Z"
output="0443a18a-5a33-4c34-aa6e-3d6fb4c16a05/SRR16105986_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b6fffe7c-652a-45ac-a6fb-68ccdc69e24a?catalog=dcp28&version=2022-04-07T19%3A28%3A10.795000Z"
output="27dc5396-721a-4d2a-8115-09d986f6f605/SRR16106089_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/b9b9fefe-9c65-4f24-a01b-617002c4ec93?catalog=dcp28&version=2022-04-07T19%3A27%3A33.439000Z"
output="6da8fa15-9c95-4099-b285-0b041745213c/SRR16105933_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fd3433de-a9f9-48f2-b967-53bacff73874?catalog=dcp28&version=2022-04-07T19%3A27%3A45.704000Z"
output="28a66651-a897-4185-98a5-001e4b15e6c8/SRR16105979_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/125cc710-0adf-451b-8e88-d07db23f5eac?catalog=dcp28&version=2022-04-07T19%3A26%3A57.363000Z"
output="7d5b2f88-b0d0-479d-b96d-405377fc61df/SRR16105784_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4436f165-527d-4b39-8e58-edf0e271a5f8?catalog=dcp28&version=2022-04-07T19%3A26%3A56.836000Z"
output="30100aa6-2029-4446-b588-2b3dff90fcec/SRR16105775_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c7a26ae7-2cf9-4baa-acfd-aeaa6eb2d825?catalog=dcp28&version=2022-04-07T19%3A27%3A54.967000Z"
output="bd7283e6-4da2-4c55-967d-ff0d1c0bd59f/SRR16106001_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a59319e1-0588-4e26-8ebd-0be496acfc07?catalog=dcp28&version=2022-04-07T19%3A27%3A32.351000Z"
output="536b9433-54d3-4fb5-a9cc-f408eb3f9ba9/SRR16105922_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f3b17999-08ca-41a8-a360-18cb0bd3c8f9?catalog=dcp28&version=2022-04-07T19%3A27%3A28.870000Z"
output="9b63f70e-9439-43d7-ae2b-ab46ec441c32/SRR16105894_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8a58d09d-d932-4e3f-9150-f1990bb2d8e8?catalog=dcp28&version=2022-04-07T19%3A26%3A59.706000Z"
output="6c902c8d-c727-4e3b-a2fa-fd8a09df9f31/SRR16105826_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08936fe8-2866-4e86-b9e0-44ac4b25606b?catalog=dcp28&version=2022-04-07T19%3A27%3A53.755000Z"
output="5937cfb9-d720-43c4-b41b-098489bde683/SRR16105993_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/49b8ad4b-5556-47f9-ba91-da06b5bbce3d?catalog=dcp28&version=2022-04-07T19%3A28%3A11.482000Z"
output="c7c1d756-e4e9-4857-8c24-ba4eaafe9507/SRR16106096_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2895290f-5e45-42a4-a2ad-471059d08783?catalog=dcp28&version=2022-04-07T19%3A27%3A57.659000Z"
output="7e85520c-1b32-440a-9296-f575ded6605d/SRR16106024_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/47918ccc-4506-4a5a-b37e-c7fa2a53deca?catalog=dcp28&version=2022-04-07T19%3A27%3A51.042000Z"
output="c5806b47-3a16-4319-baa2-dc014e981cb8/SRR16105991_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/31b9722a-1581-4702-bd9a-0013d875349e?catalog=dcp28&version=2022-04-07T19%3A27%3A53.974000Z"
output="a133413a-01da-4f8d-84df-5896b14a73d5/SRR16105994_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a14f1797-f3fd-44d4-a5df-f93f8382f1f9?catalog=dcp28&version=2022-04-07T19%3A26%3A58.021000Z"
output="9db959a4-6dac-4d4b-8380-600e074699ff/SRR16105797_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/50cb7350-3957-4b22-9ca4-81aa94da859f?catalog=dcp28&version=2022-04-07T19%3A27%3A48.863000Z"
output="38e0effd-67eb-4f48-8847-71c423a6ef28/SRR16105987_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c8ece7b2-cad5-4c63-9b89-8126a4318a5e?catalog=dcp28&version=2022-04-07T19%3A27%3A57.139000Z"
output="ef5f0bda-99b4-4dda-97bf-a986febb7166/SRR16106018_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/12b354fd-df14-4cc7-9dbb-3539558071c1?catalog=dcp28&version=2022-04-07T19%3A28%3A11.409000Z"
output="5042b694-fa2c-45ca-a0ff-72fc2cfee83e/SRR16106095_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/884d2ede-5bf8-46c4-ba9e-5426317a734a?catalog=dcp28&version=2022-04-07T19%3A28%3A12.496000Z"
output="944244ed-be4d-4d23-9686-5fd9dc627ef2/SRR16106111_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/29c1e386-9375-454c-9216-b7f6acd13b40?catalog=dcp28&version=2022-04-07T19%3A27%3A03.105000Z"
output="f3c78381-3d38-4a08-9532-1abfb93d0897/SRR16105830_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/aeee8882-662e-4cfe-afad-b02816d0654a?catalog=dcp28&version=2022-04-07T19%3A28%3A08.184000Z"
output="bb90f392-7e94-4cc6-b11c-8ed6b9e16dde/SRR16106055_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/72d1ca29-983f-43db-9bb4-f4ab2e0bf825?catalog=dcp28&version=2022-04-07T19%3A27%3A20.609000Z"
output="d674036d-63e5-4e71-8162-16c0fd41fc91/SRR16105874_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c0595257-beb9-4328-aa4f-e32a8ffdc0ca?catalog=dcp28&version=2022-04-07T19%3A28%3A10.144000Z"
output="e206212b-035b-42d1-b0f2-b70f854f7f2b/SRR16106085_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c45864a3-6e47-4975-90b6-55ee165fd6e4?catalog=dcp28&version=2022-04-07T19%3A27%3A33.697000Z"
output="03c7c566-9588-4697-a78c-75e85d70e3e5/SRR16105936_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/78742b6b-a3fc-4302-ad80-2cccef60bce5?catalog=dcp28&version=2022-04-07T19%3A26%3A59.102000Z"
output="ff2f2a8c-422e-4866-a446-634ada3bc1b9/SRR16105818_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/586539cf-c814-424c-bac3-b45c6ce67380?catalog=dcp28&version=2022-04-07T19%3A26%3A59.137000Z"
output="ef00f9c9-7d95-43e7-98cd-7e12fba5156e/SRR16105819_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/259feeda-a6f9-4703-8a25-9b72125497f7?catalog=dcp28&version=2022-04-07T19%3A27%3A54.477000Z"
output="f3303ed5-9cd3-4349-931d-3767f2f0eba0/SRR16105997_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a47aef01-4b7c-4e24-9554-e68827ed9cad?catalog=dcp28&version=2022-04-07T19%3A28%3A01.198000Z"
output="0f11ebc1-e6bc-4039-a9b5-74170fe9744f/SRR16106042_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/95cc3f7b-2205-4759-ab61-8670d4c7ed99?catalog=dcp28&version=2022-04-07T19%3A28%3A09.286000Z"
output="20efe407-47b3-4323-834f-33088f530e9f/SRR16106073_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bf1352fa-37dc-4363-8a10-df7438734e17?catalog=dcp28&version=2022-04-07T19%3A27%3A44.700000Z"
output="ea019938-5ed2-4fcd-90f5-95067bd26636/SRR16105972_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2c939b43-4cac-400e-9ee8-852cd832b8f6?catalog=dcp28&version=2022-04-07T19%3A27%3A32.740000Z"
output="cdd8b7fe-4206-4fb5-82b1-cf6ef8973cc4/SRR16105926_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ac0c469e-2deb-4b3f-8c83-e2bbf8b90ce4?catalog=dcp28&version=2022-04-07T19%3A27%3A45.888000Z"
output="76767309-75fa-48e7-82da-f8106341bfcd/SRR16105980_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/26f4baf9-b338-4899-9cab-27b9f34b9d16?catalog=dcp28&version=2022-04-07T19%3A27%3A17.197000Z"
output="74dbd63a-80a5-4cfd-b9d5-05a637ffc901/SRR16105851_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9fb952cf-fc12-44b8-914d-dadb0f13e3b3?catalog=dcp28&version=2022-04-07T19%3A27%3A24.247000Z"
output="98eab227-ffd1-439e-b93a-68c6137da6e2/SRR16105883_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2762b4ea-e81d-4936-84a0-bf1b09a03f7a?catalog=dcp28&version=2022-04-07T19%3A28%3A08.813000Z"
output="4a6953e5-a40a-4cda-a577-7c48a070d84b/SRR16106067_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/60352531-7b9c-4c7f-8492-78ce5fe8555c?catalog=dcp28&version=2022-04-07T19%3A27%3A21.375000Z"
output="2bee19a1-6841-4871-9c36-73f1f29349f9/SRR16105880_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/59137061-a5ee-4505-8842-8b34c50fd84d?catalog=dcp28&version=2022-04-07T19%3A26%3A57.970000Z"
output="e8233a1f-f0b8-4d98-a128-c09fde49478c/SRR16105795_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e2e28161-9069-4bf4-ba51-f76d31f309fe?catalog=dcp28&version=2022-04-07T19%3A27%3A42.699000Z"
output="d9e39c80-264e-44ec-81fc-c86f430742c3/SRR16105954_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c20d4258-b89b-40fe-b264-0fe1654beda1?catalog=dcp28&version=2022-04-07T19%3A28%3A11.390000Z"
output="5042b694-fa2c-45ca-a0ff-72fc2cfee83e/SRR16106095_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d2775651-96ac-47e3-b48d-e2149294dd7f?catalog=dcp28&version=2022-04-07T19%3A27%3A28.915000Z"
output="9b63f70e-9439-43d7-ae2b-ab46ec441c32/SRR16105894_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a3574f09-3b1a-4ae9-9599-072e223bc50e?catalog=dcp28&version=2022-04-07T19%3A27%3A44.318000Z"
output="3f5de3bc-b858-401c-9d40-4aa744629a87/SRR16105968_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/64bb91cd-6faf-456d-9346-99a18140beb5?catalog=dcp28&version=2022-04-07T19%3A27%3A33.402000Z"
output="6da8fa15-9c95-4099-b285-0b041745213c/SRR16105933_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0a95a802-1385-41c8-a170-d8482ddfd220?catalog=dcp28&version=2022-04-07T19%3A27%3A23.720000Z"
output="046a1865-03a8-4dcd-a6cc-795e98a42add/SRR16105882_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/33fe74dc-2403-4735-9f79-db6e851cb47f?catalog=dcp28&version=2022-04-07T19%3A28%3A12.297000Z"
output="56842abf-71b1-4f34-9655-65587315944c/SRR16106106_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/da4590bc-9633-4bbc-8f61-cd6d4f6559bc?catalog=dcp28&version=2022-04-07T19%3A27%3A22.052000Z"
output="046a1865-03a8-4dcd-a6cc-795e98a42add/SRR16105882_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c1f1d5a2-6762-4113-86b6-e028044adffc?catalog=dcp28&version=2022-04-07T19%3A26%3A56.235000Z"
output="1371b4ed-f5af-49bb-a96e-1ccfca16cad0/SRR16105760_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c747231b-fd8f-4455-bc8d-a82eb71c1f51?catalog=dcp28&version=2022-04-07T19%3A27%3A27.475000Z"
output="fb0e10ac-3443-4fad-a6fd-53dd612610a7/SRR16105885_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f9fe01eb-456e-4baa-b0eb-8b94b6c78c61?catalog=dcp28&version=2022-04-07T19%3A27%3A32.670000Z"
output="172012f0-0f31-4241-ad33-272a0efc4a75/SRR16105925_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3c511287-d674-42ad-8923-3831cad6a82f?catalog=dcp28&version=2022-04-07T19%3A27%3A56.241000Z"
output="91db17aa-c64d-4dd1-abb1-7a7301c6dfe5/SRR16106010_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ac4ab3ba-6a08-45f8-b7aa-d0b3ef855a86?catalog=dcp28&version=2022-04-07T19%3A28%3A04.657000Z"
output="220d1735-72e0-4f4d-9eac-3afaaa537e9c/SRR16106047_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f0e78bbe-8147-4f72-89cf-3ffdc04cec8d?catalog=dcp28&version=2022-04-07T19%3A27%3A15.727000Z"
output="91b3a074-511b-46f5-a745-6a020ba66cda/SRR16105840_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/540ecdc9-20e7-4932-9f4c-7cd8bd8c1288?catalog=dcp28&version=2022-04-07T19%3A26%3A58.046000Z"
output="9db959a4-6dac-4d4b-8380-600e074699ff/SRR16105797_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f803d881-ed86-4d23-9887-f244c983ddba?catalog=dcp28&version=2022-04-07T19%3A27%3A53.859000Z"
output="a133413a-01da-4f8d-84df-5896b14a73d5/SRR16105994_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3dc13c03-b99f-4642-9fdf-1054f51089e8?catalog=dcp28&version=2022-04-07T19%3A27%3A57.066000Z"
output="70b8c2de-d4e3-492c-993b-101ff35d4f7c/SRR16106017_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f6343622-4022-4730-9db4-888d7de74e63?catalog=dcp28&version=2022-04-07T19%3A27%3A49.057000Z"
output="0c3336b3-d21e-459c-a1d8-cb792a141631/SRR16105989_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/db1885b7-1bf6-438d-8b6b-d38bb7f8f832?catalog=dcp28&version=2022-04-07T19%3A27%3A56.922000Z"
output="3ed57d69-7b79-4bff-8726-68caab01fecc/SRR16106016_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/db0d8815-e761-41ed-b2df-8c34b34ef30b?catalog=dcp28&version=2022-04-07T19%3A27%3A21.146000Z"
output="b1942f46-14bb-445b-a046-de970f4924e7/SRR16105877_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/6b47129c-db2f-4ba2-b14b-a8942c409759?catalog=dcp28&version=2022-04-07T19%3A28%3A09.691000Z"
output="35059cf0-2e3e-470d-9169-7b7cbe64e56a/SRR16106078_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1667785e-4a72-4225-87f8-0a25c0acfd41?catalog=dcp28&version=2022-04-07T19%3A26%3A57.350000Z"
output="7d5b2f88-b0d0-479d-b96d-405377fc61df/SRR16105784_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c148d8d-8cd0-4eab-9387-88674bf87691?catalog=dcp28&version=2022-04-07T19%3A28%3A08.344000Z"
output="9029d12d-3d92-48e9-a135-a184dc5f7746/SRR16106058_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/96473268-5c40-4b59-9fb9-467521f9c9d8?catalog=dcp28&version=2022-04-07T19%3A27%3A44.200000Z"
output="7bc17c14-2014-4e70-aaaf-19d5d9a6e75e/SRR16105967_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/699f6fd9-45f6-4af1-a6f7-815fdfc78784?catalog=dcp28&version=2022-04-07T19%3A26%3A57.510000Z"
output="f884ff14-7e0e-407e-9992-998bd918d5ec/SRR16105787_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a162160b-1b80-4e01-82ac-e2b3cc6fd070?catalog=dcp28&version=2022-04-07T19%3A28%3A07.327000Z"
output="0d7cc23a-8b6b-43a8-8621-4ba22fb36774/SRR16106049_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5355e28c-3b32-4c8f-81dc-b43cfa51df91?catalog=dcp28&version=2022-04-07T19%3A26%3A58.229000Z"
output="96fa2c80-1471-42e8-b163-5798b01dc749/SRR16105802_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/57538814-cfd6-49f3-8187-88524f25e921?catalog=dcp28&version=2022-04-07T19%3A26%3A59.219000Z"
output="d8c88a8a-45e9-48cb-9dee-529409a3e2f5/SRR16105820_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/22fe8469-1b0f-4580-9734-7f54adb87852?catalog=dcp28&version=2022-04-07T19%3A27%3A45.215000Z"
output="6d0e8144-c29c-456a-9d30-e62929af9f33/SRR16105976_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2632d615-7381-4113-87f4-2e039a118752?catalog=dcp28&version=2022-04-07T19%3A27%3A16.107000Z"
output="0d01ab46-8ff9-4649-ac7d-c89375ea8d20/SRR16105842_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ef57b807-b706-449c-973f-516515dc2797?catalog=dcp28&version=2022-04-07T19%3A28%3A08.534000Z"
output="d1be7ef7-8edb-4dd0-be00-4692a569dff0/SRR16106061_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dd9ad483-1654-47fc-a7e7-4be7d7341d6a?catalog=dcp28&version=2022-04-07T19%3A28%3A09.980000Z"
output="949468a1-494e-4a3d-939d-03322e793ff0/SRR16106083_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f530a976-845c-4767-b1e5-24d5bf811d4f?catalog=dcp28&version=2022-04-07T19%3A27%3A44.983000Z"
output="55afffb6-c0a9-451f-9a72-21dc328340ae/SRR16105974_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/51392733-c0b8-4833-8c21-bdf815cfe348?catalog=dcp28&version=2022-04-07T19%3A27%3A56.558000Z"
output="60a8ac8a-d1f7-4521-98d8-a6d1f1d2f6d0/SRR16106012_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/51fdc29c-2691-437a-8f84-46b7cec55281?catalog=dcp28&version=2022-04-07T19%3A27%3A42.405000Z"
output="ec2cbf37-f90d-4b2b-9972-e2631e380027/SRR16105951_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/db723483-4bd7-4f1c-852e-fd23b379bb12?catalog=dcp28&version=2022-04-07T19%3A28%3A08.492000Z"
output="3b67a2e3-8952-4d16-8cef-4318535b0cce/SRR16106060_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/bb6c1b39-ed81-4ae2-93b6-51c855e9fdc7?catalog=dcp28&version=2022-04-07T19%3A26%3A56.122000Z"
output="c639013f-3adc-4f9f-97cd-965267bca80b/SRR16105757_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f0668cf0-b584-4efe-a4dc-5344f3be2d45?catalog=dcp28&version=2022-04-07T19%3A26%3A58.984000Z"
output="7c3bfac6-0cf9-444c-853b-668c48aa3f53/SRR16105816_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cf1d4582-6cc2-43e3-a0e8-177d977848aa?catalog=dcp28&version=2022-04-07T19%3A26%3A57.785000Z"
output="6691873d-a57d-4be8-bab0-27a53d83c0d9/SRR16105792_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/78d910ac-f705-484c-a1de-be4dcd9fab8d?catalog=dcp28&version=2022-04-07T19%3A28%3A08.574000Z"
output="a4492d4f-6494-4f6c-9e15-30ddec5d10da/SRR16106062_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cc7b8aaf-26a7-4736-9843-f73f5fd47ba0?catalog=dcp28&version=2022-04-07T19%3A27%3A29.974000Z"
output="c6e06e73-0d23-4764-95dc-b9952d6d9caf/SRR16105903_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7c0c95ee-19cb-4f60-8a00-b2ca6a3ca3a6?catalog=dcp28&version=2022-04-07T19%3A27%3A44.181000Z"
output="ac7679e6-c824-462c-b88c-3dc1f5b42b47/SRR16105966_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d40858f6-b02d-498d-a662-78a07cd61169?catalog=dcp28&version=2022-04-07T19%3A27%3A45.106000Z"
output="464b4273-1681-4613-87d3-822449fcd112/SRR16105975_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8afc9c15-8a26-453d-a2f1-a89c1d243b54?catalog=dcp28&version=2022-04-07T19%3A26%3A56.007000Z"
output="2ef00c65-9420-4e92-b23f-9194542914e2/SRR16105754_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3aaa4571-6a6c-4f09-882c-af4b1ac247e4?catalog=dcp28&version=2022-04-07T19%3A27%3A33.731000Z"
output="03c7c566-9588-4697-a78c-75e85d70e3e5/SRR16105936_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c9d4b0cb-97f7-4a84-bfd0-30b98eed9639?catalog=dcp28&version=2022-04-07T19%3A27%3A54.794000Z"
output="c9f2e14f-f0fb-4f6a-90cd-2ab1aa22938e/SRR16106000_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/799ac430-bcb3-47f8-8b9e-89b10fe15a14?catalog=dcp28&version=2022-04-07T19%3A27%3A48.728000Z"
output="38e0effd-67eb-4f48-8847-71c423a6ef28/SRR16105987_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/73765ac1-3eaa-486f-a1b5-31e0d65cd6e1?catalog=dcp28&version=2022-04-07T19%3A28%3A12.190000Z"
output="12d2463a-6951-430c-a01f-299db0e16b4b/SRR16106104_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ec4851f0-8946-4290-a60d-bd6f051328c4?catalog=dcp28&version=2022-04-07T19%3A27%3A28.838000Z"
output="7f951a6e-5541-45d8-bca2-ca3477480664/SRR16105893_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/00301988-c66b-4fa2-8023-c371401da87f?catalog=dcp28&version=2022-04-07T19%3A27%3A30.372000Z"
output="0098acb4-e41d-497d-b7c6-d754a1960474/SRR16105907_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/1b64ee64-e861-4c21-bbd6-21c26c9a7be1?catalog=dcp28&version=2022-04-07T19%3A27%3A32.093000Z"
output="8de660b1-fa9e-48da-9d7d-ce171d684923/SRR16105920_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/94c7a882-1c07-4add-b17a-b8701117bc0f?catalog=dcp28&version=2022-04-07T19%3A28%3A12.350000Z"
output="bc8373a3-3f43-4498-b083-7eca3f757c69/SRR16106107_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/66c58ea9-7ca4-40dc-91bd-4958b3da0be7?catalog=dcp28&version=2022-04-07T19%3A27%3A43.229000Z"
output="4591937f-51c1-4e7b-984d-b5a831e72cfd/SRR16105961_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e9062338-f7b3-4af0-a4f4-bb9dcaef6327?catalog=dcp28&version=2022-04-07T19%3A27%3A15.964000Z"
output="76722270-1b19-4a3d-a588-6747d894cab0/SRR16105841_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/253b3288-4783-40c3-9eb5-ca30f0cb3b22?catalog=dcp28&version=2022-04-07T19%3A26%3A59.523000Z"
output="c7a45e4a-bc9c-49d9-85c9-98bfabe148b8/SRR16105824_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/786294d4-18bf-4361-9618-ab0c66234ded?catalog=dcp28&version=2022-04-07T19%3A27%3A36.866000Z"
output="16b37a5b-1e60-41e4-9c89-3a9cf352cd34/SRR16105941_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c44706c8-4296-49d7-a038-47c6fabb2b7d?catalog=dcp28&version=2022-04-07T19%3A26%3A56.579000Z"
output="31806f69-282e-40a1-9204-98ab7bd60d0f/SRR16105768_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c9cb1324-7df5-403a-a49b-6bad1c3ec5b7?catalog=dcp28&version=2022-04-07T19%3A26%3A57.206000Z"
output="2407f163-90e5-4aad-8944-837e4f541a74/SRR16105780_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/329297cb-20af-4343-b0ea-791c095a1586?catalog=dcp28&version=2022-04-07T19%3A27%3A29.452000Z"
output="b4a55412-3273-4137-869f-68a93521fe25/SRR16105897_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f5f943b5-566e-4501-9f68-8d39daa15401?catalog=dcp28&version=2022-04-07T19%3A27%3A30.066000Z"
output="4e0e7092-b395-4524-818f-d294a98e2fa9/SRR16105904_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fab5af52-a1d1-41e5-9052-45db934149e3?catalog=dcp28&version=2022-04-07T19%3A26%3A56.475000Z"
output="6ccb5aa6-da53-4de9-97ec-e0858905a2ce/SRR16105766_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7818ce69-e2d9-4b5e-9f5d-094f9f5fe3d5?catalog=dcp28&version=2022-04-07T19%3A28%3A10.186000Z"
output="e206212b-035b-42d1-b0f2-b70f854f7f2b/SRR16106085_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2b8a2575-f3cc-4a7e-a7ae-935a2096227a?catalog=dcp28&version=2022-04-07T19%3A27%3A56.598000Z"
output="4f14f89d-2083-4b95-b5b2-10e20b80484b/SRR16106013_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/39aed6c4-9019-458d-a75b-a0bbfd176e14?catalog=dcp28&version=2022-04-07T19%3A27%3A35.888000Z"
output="ba6d0a59-079c-4cac-8d44-1777c77d2e07/SRR16105940_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/663bde83-83f5-4a52-868f-19ed0d7243f2?catalog=dcp28&version=2022-04-07T19%3A27%3A16.495000Z"
output="58c697f6-f768-4945-a107-055de56fe6b2/SRR16105845_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/29fc0c9a-3716-4cdf-b595-7d294f60c788?catalog=dcp28&version=2022-04-07T19%3A28%3A01.236000Z"
output="cd69f208-db53-4efd-a474-035ce10620a4/SRR16106043_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3aefeb7c-0756-44ba-9d91-5620c7340989?catalog=dcp28&version=2022-04-07T19%3A26%3A56.110000Z"
output="c639013f-3adc-4f9f-97cd-965267bca80b/SRR16105757_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/eef1106b-ae71-45e9-9e77-ecf583e4b3e5?catalog=dcp28&version=2022-04-07T19%3A27%3A57.254000Z"
output="126091f4-7045-4a8c-9a21-4f5970252b90/SRR16106019_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/36aa5850-ca96-4ddb-83a5-802b0d257682?catalog=dcp28&version=2022-04-07T19%3A27%3A19.336000Z"
output="941885c8-4d6c-4824-bdc2-a61c29e1251e/SRR16105865_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7db84605-7cf5-4fee-9c11-5beab9b4ceaf?catalog=dcp28&version=2022-04-07T19%3A28%3A09.502000Z"
output="d2749e92-59b1-4bf8-a5aa-bf79ab36a671/SRR16106075_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/60dca9b9-6a4a-43e1-b7af-ec4be96f9508?catalog=dcp28&version=2022-04-07T19%3A27%3A44.478000Z"
output="8f9ec997-f531-4f77-a32b-7e356a96daa5/SRR16105970_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/268ce2fa-0631-40db-afc9-3cbdc71f1b64?catalog=dcp28&version=2022-04-07T19%3A27%3A16.391000Z"
output="0d27c127-1fea-4f7b-b54e-4a7a06d8b1cc/SRR16105844_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/f8028584-24aa-4d6c-a211-0442122cc5f3?catalog=dcp28&version=2022-04-07T19%3A27%3A37.318000Z"
output="d49f7948-f3c6-4fcd-8552-43d0e4ade6c1/SRR16105943_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fa6113bc-9f16-484a-bf3e-76ac18fd3ef5?catalog=dcp28&version=2022-04-07T19%3A28%3A08.226000Z"
output="a1402ec5-dcbb-4fe0-84df-2d92e26273b9/SRR16106056_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dd3ba99d-3736-4dbe-95f4-2182058660be?catalog=dcp28&version=2022-04-07T19%3A26%3A56.375000Z"
output="971a0dd5-bb0d-49d9-b7f7-bfd4fc5fe4fc/SRR16105763_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dccfd119-a698-4402-ab36-37a8c8f72f3a?catalog=dcp28&version=2022-04-07T19%3A26%3A56.463000Z"
output="6bf6781c-1dd4-4f8a-a4c4-7314cbe642f0/SRR16105765_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/43d32ed2-502b-4502-b0f7-0212fe983efc?catalog=dcp28&version=2022-04-07T19%3A26%3A58.610000Z"
output="1136f513-4add-4317-ab09-61535c5ef07b/SRR16105809_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/69051b92-9143-47b4-9768-dde28e7c0d0f?catalog=dcp28&version=2022-04-07T19%3A28%3A00.780000Z"
output="bd3f8f43-09c9-4df0-8ce5-0f57f98f1c3a/SRR16106038_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/72b9cea2-c6ec-42ba-9ef4-ce294c1a5198?catalog=dcp28&version=2022-04-07T19%3A27%3A17.850000Z"
output="f9f906cb-3cf3-442d-b264-17b53181fee3/SRR16105856_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c8c608a4-04b3-482a-9216-b515e37b5e69?catalog=dcp28&version=2022-04-07T19%3A27%3A32.913000Z"
output="8aeb0ebd-285a-424a-94b6-e9715786c1c2/SRR16105928_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5c648019-bd65-4b18-844d-0c1b0f652814?catalog=dcp28&version=2022-04-07T19%3A26%3A58.383000Z"
output="ee1a5d8f-b801-4f53-8ef4-a2840105e89a/SRR16105806_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ac33790f-abb5-4c80-815b-a31929e201b5?catalog=dcp28&version=2022-04-07T19%3A26%3A59.087000Z"
output="ff2f2a8c-422e-4866-a446-634ada3bc1b9/SRR16105818_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/91f95eb7-c5b9-41c1-88c1-5a85bc78f3e7?catalog=dcp28&version=2022-04-07T19%3A27%3A32.937000Z"
output="8aeb0ebd-285a-424a-94b6-e9715786c1c2/SRR16105928_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7528e20b-cb8d-47e8-a6a8-950415978d32?catalog=dcp28&version=2022-04-07T19%3A28%3A12.437000Z"
output="6197baee-5ca1-499c-a46f-2d3dee3ebe73/SRR16106110_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2ae784db-c082-4421-98cf-8e77f6056207?catalog=dcp28&version=2022-04-07T19%3A27%3A18.833000Z"
output="d710d243-2db1-443d-b9d5-b8079b3df6bc/SRR16105864_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/10fa4dd4-9400-4791-8b95-b745ca126cc6?catalog=dcp28&version=2022-04-07T19%3A27%3A25.448000Z"
output="98eab227-ffd1-439e-b93a-68c6137da6e2/SRR16105883_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5aac2c56-6ac4-4c9e-8c51-4e004f2eae7a?catalog=dcp28&version=2022-04-07T19%3A27%3A18.666000Z"
output="4f1e110d-76b3-4ede-bd03-1a1b7a5060ba/SRR16105863_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/30d476be-68b4-4a02-9af3-fb8ae2e38017?catalog=dcp28&version=2022-04-07T19%3A26%3A57.302000Z"
output="5e801b90-8c49-44b3-b703-9a5b073f07a5/SRR16105783_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7f1a513a-cbf5-4e90-9622-6d3a17f50609?catalog=dcp28&version=2022-04-07T19%3A28%3A12.617000Z"
output="7e3af873-a224-4f4f-8b19-85093eafe0fc/SRR16106115_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/681e1aa7-2dde-41a3-8f96-f1f98f808634?catalog=dcp28&version=2022-04-07T19%3A28%3A12.593000Z"
output="6cd2b7d8-56e9-4ea4-aee8-9eac4c8948d2/SRR16106114_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e2d9d669-d096-4fd0-b787-7bc43f9aa460?catalog=dcp28&version=2022-04-07T19%3A27%3A29.228000Z"
output="f13ff253-8785-47e8-805a-1a5a08ae8345/SRR16105895_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9a026abd-57d6-4912-a8c3-8f516062cb48?catalog=dcp28&version=2022-04-07T19%3A27%3A29.947000Z"
output="c6e06e73-0d23-4764-95dc-b9952d6d9caf/SRR16105903_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/951fd6ed-5924-4f24-8b96-f31f2d28d02f?catalog=dcp28&version=2022-04-07T19%3A27%3A32.646000Z"
output="172012f0-0f31-4241-ad33-272a0efc4a75/SRR16105925_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/90885f7b-516a-44ef-abc7-726790def6b9?catalog=dcp28&version=2022-04-07T19%3A27%3A10.817000Z"
output="ae48556e-60dc-4ad4-9096-e2421da4586c/SRR16105836_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9fb2e758-c10c-4818-aaba-a85783f63f5c?catalog=dcp28&version=2022-04-07T19%3A27%3A17.061000Z"
output="1b104e22-8f01-4954-927f-adc907a91382/SRR16105850_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/29fd7bef-889a-4a3b-b056-0dd96fc294c7?catalog=dcp28&version=2022-04-07T19%3A27%3A42.367000Z"
output="45a1481c-a462-4b18-9dd3-0bdf6ad981e0/SRR16105950_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3dd0017d-7f61-4e7a-bc72-95446a2f84f8?catalog=dcp28&version=2022-04-07T19%3A27%3A53.587000Z"
output="5937cfb9-d720-43c4-b41b-098489bde683/SRR16105993_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0c672359-2297-4e47-826d-5d14d5420d83?catalog=dcp28&version=2022-04-07T19%3A26%3A56.361000Z"
output="971a0dd5-bb0d-49d9-b7f7-bfd4fc5fe4fc/SRR16105763_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3b1ad13c-61a9-4222-bfe2-48655313103f?catalog=dcp28&version=2022-04-07T19%3A27%3A43.281000Z"
output="4591937f-51c1-4e7b-984d-b5a831e72cfd/SRR16105961_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ab52add3-09cf-4e6e-9b6e-a99afea05c71?catalog=dcp28&version=2022-04-07T19%3A27%3A57.952000Z"
output="da6cf693-ad4d-440a-a0e7-698653151e44/SRR16106028_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/cdea69b0-5e25-4c20-be3f-19dfab07dc14?catalog=dcp28&version=2022-04-07T19%3A27%3A56.521000Z"
output="60a8ac8a-d1f7-4521-98d8-a6d1f1d2f6d0/SRR16106012_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/37adfe7d-2ba0-4ccd-975e-b89ba27068de?catalog=dcp28&version=2022-04-07T19%3A26%3A58.075000Z"
output="88855126-fc0c-480f-822b-0ff3779c92bd/SRR16105798_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/618c67c4-3df5-4218-b086-fc13b1250670?catalog=dcp28&version=2022-04-07T19%3A27%3A43.900000Z"
output="560607c8-3d51-4dd2-866f-4c09fb872727/SRR16105963_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5568cc7d-82a7-427b-aa78-cf4248082d48?catalog=dcp28&version=2022-04-07T19%3A28%3A09.907000Z"
output="e1f958f3-7f7d-41d0-8551-a82103e09c4d/SRR16106082_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/53c2f92b-263d-48c9-9ddd-2577378dc839?catalog=dcp28&version=2022-04-07T19%3A27%3A18.809000Z"
output="4f1e110d-76b3-4ede-bd03-1a1b7a5060ba/SRR16105863_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9c108ae2-3f12-4f85-bf89-46711384dc89?catalog=dcp28&version=2022-04-07T19%3A28%3A00.944000Z"
output="2fdb0a8d-4d67-48f7-947b-e377f91e3d6a/SRR16106040_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5f79d729-102d-40f1-bd71-f3867722639d?catalog=dcp28&version=2022-04-07T19%3A27%3A44.449000Z"
output="8f9ec997-f531-4f77-a32b-7e356a96daa5/SRR16105970_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2367215c-f59e-48e6-be79-0afcca267b94?catalog=dcp28&version=2022-04-07T19%3A27%3A17.126000Z"
output="1b104e22-8f01-4954-927f-adc907a91382/SRR16105850_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7e24d5d8-0f16-47e4-b8eb-95bdbc915d32?catalog=dcp28&version=2022-04-07T19%3A27%3A49.286000Z"
output="514875d8-b2fc-4453-a4a9-ce2f052cdb78/SRR16105990_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8796d6dd-45ba-48df-83db-610db1af130a?catalog=dcp28&version=2022-04-07T19%3A27%3A55.058000Z"
output="724c2f24-6739-40b4-be89-3c69c7ede75a/SRR16106002_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2855fc3a-3889-4102-b323-b1ee037913ec?catalog=dcp28&version=2022-04-07T19%3A27%3A31.684000Z"
output="20a8abe3-c25c-4736-a244-d66f6fd0ae91/SRR16105915_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0bb7b833-d185-4920-8329-4515ccf3ded3?catalog=dcp28&version=2022-04-07T19%3A26%3A56.209000Z"
output="0dab1345-3f9c-45c6-a429-671708f38f52/SRR16105759_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7ac38398-16dd-4ca6-99b5-4750f84b17cf?catalog=dcp28&version=2022-04-07T19%3A28%3A05.887000Z"
output="975d507d-3c7e-41f6-905e-93e9460d3108/SRR16106048_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2b646cc7-97b7-49fe-808d-efa47d50206c?catalog=dcp28&version=2022-04-07T19%3A26%3A57.498000Z"
output="f884ff14-7e0e-407e-9992-998bd918d5ec/SRR16105787_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/47fb2234-af1e-4999-9621-b5db01d7d028?catalog=dcp28&version=2022-04-07T19%3A27%3A43.162000Z"
output="37a8cdd4-737e-412f-9a42-5c8ea15a7745/SRR16105960_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0c848d21-3efc-4ac0-9772-5d017ac2eb16?catalog=dcp28&version=2022-04-07T19%3A28%3A07.967000Z"
output="8af57556-1650-4217-a4e0-c76a67224a71/SRR16106053_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dbdf4dc8-9662-4fb0-ab48-efe45db78b23?catalog=dcp28&version=2022-04-07T19%3A27%3A45.142000Z"
output="464b4273-1681-4613-87d3-822449fcd112/SRR16105975_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/801db1cc-31b8-4268-a471-149b9eb0ba26?catalog=dcp28&version=2022-04-07T19%3A27%3A01.683000Z"
output="175d983d-e177-44a6-9bcf-dbc121e48b0b/SRR16105829_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/ee78d66f-101a-44f7-b592-38d2fedfef30?catalog=dcp28&version=2022-04-07T19%3A28%3A07.449000Z"
output="db2ac85a-6c6c-4f1b-a7bc-8eaf8b1fd124/SRR16106050_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/32b34dc9-5626-44e6-bd59-8db98489c3c0?catalog=dcp28&version=2022-04-07T19%3A27%3A45.468000Z"
output="ac214f2f-64cb-45be-bcd8-1957b48ea0c8/SRR16105978_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/333062bb-0895-4c47-a38c-98c62a83a47d?catalog=dcp28&version=2022-04-07T19%3A28%3A08.280000Z"
output="524efc57-19c1-4878-b2a3-c360f140d4f9/SRR16106057_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3ddaf760-6b5c-40ad-a4b9-ff76803c386f?catalog=dcp28&version=2022-04-07T19%3A27%3A54.918000Z"
output="bd7283e6-4da2-4c55-967d-ff0d1c0bd59f/SRR16106001_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/2f1c318b-af5f-43ba-8624-40963e18410a?catalog=dcp28&version=2022-04-07T19%3A28%3A04.053000Z"
output="e703efca-f439-45e7-989a-51e9219896b4/SRR16106046_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9e231295-5cd4-4fa4-bfe0-2deca9a18d5a?catalog=dcp28&version=2022-04-07T19%3A26%3A56.776000Z"
output="25d1cb64-8f8a-4593-a647-9a12bf33ca81/SRR16105774_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d83d556e-a5d6-4150-84f2-91a865ba3b12?catalog=dcp28&version=2022-04-07T19%3A27%3A17.343000Z"
output="11b42c9c-454b-4313-b996-09d5c32dc89c/SRR16105852_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5711f5f3-0932-4018-970b-e54bcdf18f9e?catalog=dcp28&version=2022-04-07T19%3A27%3A57.725000Z"
output="584cbf84-929a-4d8a-acd4-606ecff0694c/SRR16106025_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fcab2af8-b561-4dac-9840-269cad858305?catalog=dcp28&version=2022-04-07T19%3A27%3A16.177000Z"
output="0d01ab46-8ff9-4649-ac7d-c89375ea8d20/SRR16105842_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/e6ceb5d8-427d-4109-8eb3-8c99aa09f52e?catalog=dcp28&version=2022-04-07T19%3A27%3A27.981000Z"
output="c9ee4eac-15d3-410a-8ba8-8926fe8d4fcb/SRR16105889_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/62c6a936-f5f2-46ab-8037-218e916007a6?catalog=dcp28&version=2022-04-07T19%3A27%3A56.010000Z"
output="b1211531-2be2-448b-b806-e137b07d779c/SRR16106008_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/dae1f9dd-206c-4681-bcdb-488bb184cde2?catalog=dcp28&version=2022-04-07T19%3A28%3A08.912000Z"
output="ac70ba6e-eb5f-49b4-9dd3-c8c7987429f3/SRR16106069_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d8041865-a68a-407f-92a8-d78a44f30dae?catalog=dcp28&version=2022-04-07T19%3A26%3A59.449000Z"
output="ea20a490-8a70-46ed-aa47-df4cb27c25cd/SRR16105823_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/50895700-82f2-4f3e-b9a2-6711a5b56d94?catalog=dcp28&version=2022-04-07T19%3A27%3A20.653000Z"
output="d674036d-63e5-4e71-8162-16c0fd41fc91/SRR16105874_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4210158a-3310-40db-b3a4-6ad95006cae3?catalog=dcp28&version=2022-04-07T19%3A27%3A43.794000Z"
output="b053b90f-9396-4c5d-ae9d-76876452d688/SRR16105962_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4f332ec2-fc8f-4bb4-ab53-8c121d522ca5?catalog=dcp28&version=2022-04-07T19%3A26%3A58.537000Z"
output="cfe1f1f6-6e1f-46d4-85ed-e516440be211/SRR16105808_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/99e33226-11ec-4f95-9523-bf3b0adeec84?catalog=dcp28&version=2022-04-07T19%3A27%3A42.824000Z"
output="998ae609-7c67-4ff9-afe7-bfd518484e60/SRR16105956_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/82d7d9f0-71df-4675-980c-b7969f68b57e?catalog=dcp28&version=2022-04-07T19%3A27%3A56.214000Z"
output="91db17aa-c64d-4dd1-abb1-7a7301c6dfe5/SRR16106010_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/00a31992-9211-4552-8189-9182faadaed9?catalog=dcp28&version=2022-04-07T19%3A28%3A08.886000Z"
output="ac70ba6e-eb5f-49b4-9dd3-c8c7987429f3/SRR16106069_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d731d7ac-bc9b-4f78-b919-a83b0ed51f12?catalog=dcp28&version=2022-04-07T19%3A28%3A04.288000Z"
output="220d1735-72e0-4f4d-9eac-3afaaa537e9c/SRR16106047_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/0aab34a8-2acc-4f74-bb82-f111b328981b?catalog=dcp28&version=2022-04-07T19%3A26%3A56.605000Z"
output="6190457d-00eb-41cb-b11e-c6e06604f58f/SRR16105769_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/7506792d-8d1e-4e67-abc8-1973f154df38?catalog=dcp28&version=2022-04-07T19%3A26%3A56.539000Z"
output="26747c63-f381-4b99-9d8a-04d79f36e779/SRR16105767_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/c3756c1a-122c-4218-acc4-e05140117096?catalog=dcp28&version=2022-04-07T19%3A26%3A58.965000Z"
output="7c3bfac6-0cf9-444c-853b-668c48aa3f53/SRR16105816_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/5680145f-922f-4a3e-b682-75b6a37f0933?catalog=dcp28&version=2022-04-07T19%3A27%3A31.787000Z"
output="1c4fe4d7-ac3c-4cb8-befc-d84b3990091f/SRR16105916_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/229f60e2-36bc-44f0-af3a-028d23109524?catalog=dcp28&version=2022-04-07T19%3A26%3A57.181000Z"
output="f2eac87b-df1f-4620-ae7d-69d4a36700d3/SRR16105779_R2.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/a22c14ca-d0e3-4010-bc2e-8db36f6d66c8?catalog=dcp28&version=2022-04-07T19%3A26%3A56.629000Z"
output="a678f0bd-c71d-4557-a524-90f6f0ec7f78/SRR16105770_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/acedb8cd-40a0-4390-ac1c-15d17ae21514?catalog=dcp28&version=2022-04-07T19%3A27%3A18.498000Z"
output="cf82af2c-ab88-4b88-8211-679f41f97abc/SRR16105862_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/8f753352-2dd7-43c4-8588-d8914b6492a0?catalog=dcp28&version=2022-04-07T19%3A27%3A31.928000Z"
output="0386a58f-f2a9-4a8d-b0a5-1f5e954bcbd7/SRR16105918_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/999afbc0-0dd4-409f-ba2f-e9faac990a51?catalog=dcp28&version=2022-04-07T19%3A27%3A30.092000Z"
output="4e0e7092-b395-4524-818f-d294a98e2fa9/SRR16105904_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d6103599-5adf-4ac6-bfdc-be2bcb4fc5ae?catalog=dcp28&version=2022-04-07T19%3A27%3A27.830000Z"
output="59d9a2bd-f41c-4cb7-8d94-61d8ae1588f0/SRR16105888_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/08c11ee2-822e-4f57-b7b4-3a9edd73e017?catalog=dcp28&version=2022-04-07T19%3A27%3A57.830000Z"
output="d5bc19e9-bd96-4e17-951c-d5edeaeb4d99/SRR16106027_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/19f3b3a2-763d-4e72-a5c2-3d7e83af64f5?catalog=dcp28&version=2022-04-07T19%3A26%3A57.958000Z"
output="e8233a1f-f0b8-4d98-a128-c09fde49478c/SRR16105795_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/9d236ba0-696b-48f0-af48-9cd6eefd0020?catalog=dcp28&version=2022-04-07T19%3A28%3A09.383000Z"
output="2c9e75b6-f9fa-453f-9caa-e445e50c2e5d/SRR16106074_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/fe28f3da-f335-46f0-8a82-ef6fa91c7c23?catalog=dcp28&version=2022-04-07T19%3A27%3A39.336000Z"
output="759fef86-2f91-42e4-9122-f4ef6e3fdeac/SRR16105945_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/4ee2b199-ef36-488f-89bd-a1faf5bccf25?catalog=dcp28&version=2022-04-07T19%3A26%3A58.836000Z"
output="a6c579bc-a1fd-4e2f-8848-d7fa40ecada9/SRR16105813_R1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/3db6675c-d3d4-426e-950a-c533f80c7fa7?catalog=dcp28&version=2022-04-07T19%3A27%3A30.898000Z"
output="9d93665a-8355-41d3-bb89-e61678ad7437/SRR16105912_I1.fastq.gz"

url="https://service.azul.data.humancellatlas.org/repository/files/d31528da-dfe0-40ae-973d-dc08c6779f82?catalog=dcp28&version=2022-04-07T19%3A27%3A49.238000Z"
output="514875d8-b2fc-4453-a4a9-ce2f052cdb78/SRR16105990_I1.fastq.gz"

"""

ids = ['SRR16105824', 'SRR16105825', 'SRR16105826', 'SRR16105827', 'SRR16105828', 'SRR16105829', 'SRR16105830', 'SRR16105831', 'SRR16105832', 'SRR16105833', 'SRR16105834', 'SRR16105835', 'SRR16105777', 'SRR16105778', 'SRR16105779', 'SRR16105780', 'SRR16105781', 'SRR16105782', 'SRR16105783', 'SRR16105784', 'SRR16105785', 'SRR16105786', 'SRR16105787', 'SRR16105788', 'SRR16105881', 'SRR16105882', 'SRR16105883', 'SRR16105884', 'SRR16105885', 'SRR16105886', 'SRR16105887', 'SRR16105888', 'SRR16105889', 'SRR16105890', 'SRR16105891', 'SRR16105892', 'SRR16105959', 'SRR16105960', 'SRR16105961', 'SRR16105962', 'SRR16105963', 'SRR16105964', 'SRR16105965', 'SRR16105966', 'SRR16105967', 'SRR16105968', 'SRR16105969', 'SRR16105970', 'SRR16105972', 'SRR16105973', 'SRR16105974', 'SRR16105975', 'SRR16105976', 'SRR16105977', 'SRR16105978', 'SRR16105979', 'SRR16105980', 'SRR16105981', 'SRR16105982', 'SRR16105983', 'SRR16106076', 'SRR16106077', 'SRR16106078', 'SRR16106079', 'SRR16106080', 'SRR16106081', 'SRR16106082', 'SRR16106083', 'SRR16106084', 'SRR16106085', 'SRR16106086', 'SRR16106099', 'SRR16105948', 'SRR16105949', 'SRR16105950', 'SRR16105951', 'SRR16105952', 'SRR16105953', 'SRR16105954', 'SRR16105955', 'SRR16105956', 'SRR16105957', 'SRR16105958', 'SRR16105971', 'SRR16105789', 'SRR16105790', 'SRR16105791', 'SRR16105792', 'SRR16105793', 'SRR16105794', 'SRR16105795', 'SRR16105796', 'SRR16105808', 'SRR16105809', 'SRR16105810', 'SRR16105811', 'SRR16105812', 'SRR16105813', 'SRR16105814', 'SRR16105823', 'SRR16106108', 'SRR16106109', 'SRR16106110', 'SRR16106111', 'SRR16106112', 'SRR16106113', 'SRR16106114', 'SRR16106115']
urls = []
temp = []
for i in script.split('\n'):
    if 'url' in i:
        temp.append(i)
    if 'output' in i:
        temp.append(i)
        urls.append(temp)
        temp=[]

link=[]
ouput=[]
for i in urls:
    for id in ids:
        if id in i[1]:
            link.append(i[0])
            ouput.append(i[1])

for i in link:
    #print(i[-24:-1])
    i=i.replace('"','')
    i=i.replace('url=','')
    print(i)
print(len(link))