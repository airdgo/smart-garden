"""Add SensorReadings model

Revision ID: 5abfbdde8f8a
Revises: e2412789c190
Create Date: 2024-05-26 11:00:51.852459

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '5abfbdde8f8a'
down_revision = 'e2412789c190'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sensorreading',
    sa.Column('soil_humidity', sa.Float(), nullable=False),
    sa.Column('air_humidity', sa.Float(), nullable=False),
    sa.Column('pressure', sa.Float(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('uv_index', sa.Float(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sensorreading')
    # ### end Alembic commands ###
