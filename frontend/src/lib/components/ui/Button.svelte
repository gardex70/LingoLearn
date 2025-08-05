<script lang="ts">
    type Variant = 'primary' | 'secondary' | 'outline';
    type Size = 'small' | 'medium' | 'large' | 'fullWidth';

    interface ButtonProps {
        children: any;
        variant?: Variant;
        size?: Size;
        [key: string]: unknown; // permite desconstruir {...rest}
    }

    let {
        children,
        variant = 'primary',
        size = 'medium',
        ...rest
    }: ButtonProps = $props();
</script>

<button
    class="btn"
    class:primary={variant === 'primary'}
    class:secondary={variant === 'secondary'}
    class:outline={variant === 'outline'}
    class:small={size === 'small'}
    class:medium={size === 'medium'}
    class:large={size === 'large'}
    class:fullWidth={size === 'fullWidth'}
    {...rest}
>
    {@render children()}
</button>

<style>
    button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.2s ease;
        cursor: pointer;
        border: none;
        outline: none;
        font-family: inherit;
    }

    button:disabled {
        opacity: 0.6;
        cursor: not-allowed;
    }

/* Variants */
    .primary {
        background: var(--primary-blue);
        color: white;
    }

    .primary:hover:not(:disabled) {
        background: var(--primary-blue-hover);
        transform: translateY(-1px);
    }

    .outline {
        background: transparent;
        color: var(--primary-blue);
        border: 1px solid var(--primary-blue);
    }

    .outline:hover:not(:disabled) {
        background: var(--primary-blue-light);
    }

/* Sizes */
.small {
  padding: 0.5rem 0.75rem;
  font-size: 0.875rem;
}

.medium {
  padding: 0.75rem 1rem;
  font-size: 1rem;
}

.large {
  padding: 1rem 1.5rem;
  font-size: 1.1rem;
}

.fullWidth {
  width: 100%;
}
</style>