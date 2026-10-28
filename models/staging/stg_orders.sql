with

source as (
    select * from {{ ref('raw_orders') }}
),

renamed as (

    select
        ID as order_id,
        CUSTOMER as customer_id,
        timestamp(ORDERED_AT) as order_date,
        STORE_ID as store_id,
        
        -- Sửa 3 dòng dưới đây để đổi từ Xu sang Đô-la:
        {{ cents_to_dollars('SUBTOTAL') }} as subtotal,
        {{ cents_to_dollars('TAX_PAID') }} as tax_paid,
        {{ cents_to_dollars('ORDER_TOTAL') }} as order_total

    from source

)

select * from renamed