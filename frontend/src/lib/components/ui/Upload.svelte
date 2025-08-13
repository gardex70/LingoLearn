<script lang="ts">
	import { UploadIcon } from "@lucide/svelte";
	import { Button } from "$lib/components/ui";

    let fileInput: HTMLInputElement | undefined = $state();
	
	interface UploadProps {
		onUpload: (fileContent: string) => void
	}

	let { onUpload }: UploadProps = $props();

    async function handleFileSelect(event: Event) {
		const target = event.target as HTMLInputElement;
		if (!target.files) return;

		const file = target.files[0];
		const fileContent = await file.text();
		
		onUpload(fileContent);
	}

</script>

<div class="upload" onclick={() => fileInput?.click()} aria-hidden="true">
    <UploadIcon size={48} color={"var(--text-secondary)"}/>
    <div class="upload-text">
        <h3>Arraste e solte seus arquivos aqui</h3>
        <p>Ou clique para selecionar arquivos</p>
    </div>
    <Button size='small'>Selecionar Livro</Button>

    <input
		type="file"
		accept=".pdf,.epub,.txt"
		bind:this={fileInput}
		onchange={handleFileSelect}
		hidden
	/>
</div>


<style>
    .upload {
        display: flex;
        gap: 1rem;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        background: var(--background-gray);
        border-radius: 6px;
        outline: 2px dashed var(--border-focus);
    }

    .upload-text {
        text-align: center;
    }

</style>